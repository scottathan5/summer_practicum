import streamlit as st
import pandas as pd
import pickle

@st.cache_resource
def load_model():
    try:
        with open("piedmontapp.pkl", "rb") as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Ensure 'mountainapp.pkl' is pushed to GitHub.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

pipeline = load_model()

st.title("Piedmont/Central Airbnb Profit Predictor")
st.write("Enter listing details to estimate revenue:")

# Input selectors
MONTH_MAP = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}
selected_month_str = st.selectbox("Select start month", list(MONTH_MAP.keys()))
selected_month = MONTH_MAP[selected_month_str]

REGION = ('Mountain', 'Piedmont/Central', 'Beach')
selected_region = st.selectbox("Select region", REGION)

TYPE = ('entire_home', 'hotel_room', 'unique_location', 'private_room')
room_type = st.selectbox("Select room type", TYPE)

photo_count = st.number_input("Number of photos planned", min_value=0, value=20, step=1)
guest_count = st.number_input("Guest capacity", min_value=1, value=4, step=1)
bedroom = st.number_input("Number of bedrooms", min_value=0, value=2, step=1)
beds = st.number_input("Number of beds", min_value=0, value=2, step=1)
baths = st.number_input("Number of bathrooms", min_value=0.0, value=1.5, step=0.5)

managed_str = st.selectbox("Will it be professionally managed?", ('True', 'False'))
managed = True if managed_str == 'True' else False

nights = st.number_input("Minimum stay (nights)", min_value=1, value=2, step=1)

CITIES = ('Asheville', 'Carolina Beach', 'Charlotte', 'Durham', 'Gatlinburg',
          'Myrtle Beach', 'Pigeon Forge', 'Raleigh', 'Williamsburg', 'Wilmington')
city = st.selectbox("City location", CITIES)

if st.button("Predict Revenue"):
    if pipeline is None:
        st.error("Model is not loaded.")
    else:
        # Create single-row DataFrame matching raw training columns
        input_data = pd.DataFrame({
            "STARTmonth": [selected_month],
            "region_x": [selected_region],
            "room_type": [room_type],
            "photos_count": [photo_count],
            "guests": [guest_count],
            "bedrooms": [bedroom],
            "beds": [beds],
            "baths": [baths],
            "professional_management": [managed],
            "min_nights": [nights],
            "City": [city]
        })

        # Apply same get_dummies transformation used in training notebook
        input_encoded = pd.get_dummies(
            input_data, 
            columns=['STARTmonth', 'region_x', 'room_type', 'City'], 
            drop_first=True
        )

        # Retrieve feature names saved in the pipeline's scaler or model step
        try:
            model_features = pipeline.named_steps['scaler'].feature_names_in_
        except AttributeError:
            model_features = getattr(pipeline, "feature_names_in_", None)

        if model_features is not None:
            # Reindex to enforce exact training column ordering and fill missing dummy columns with 0
            input_encoded = input_encoded.reindex(columns=model_features, fill_value=0)
            
            # Predict
            prediction = pipeline.predict(input_encoded)[0]
            st.success(f"Estimated Monthly Revenue: **${prediction:,.2f}**")
        else:
            st.error("Feature names could not be loaded from pipeline. Re-export model using a Pipeline.")
