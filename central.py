import streamlit as st
import pandas as pd
import pickle

@st.cache_resource
def load_model():
    try:
        with open("piedmont.pkl", "rb") as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Ensure 'beach.pkl' is present in your repo.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

pipeline = load_model()

st.title("Beach Airbnb Profit Predictor")
st.write("Enter listing details to estimate revenue:")

# Input selectors
MONTH_MAP = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}
selected_month_str = st.selectbox("Select start month", list(MONTH_MAP.keys()))
selected_month = MONTH_MAP[selected_month_str]

TYPE = ('entire_home', 'hotel_room', 'unique_location', 'private_room')
room_type = st.selectbox("Select room type", TYPE)

photo_count = st.number_input("Number of photos planned", min_value=0, value=20, step=1)
guest_count = st.number_input("Guest capacity", min_value=1, value=4, step=1)
bedroom = st.number_input("Number of bedrooms", min_value=0, value=2, step=1)
beds = st.number_input("Number of beds", min_value=0, value=2, step=1)
baths = st.number_input("Number of bathrooms", min_value=0.0, value=1.5, step=0.5)

managed_str = st.selectbox("Will it be professionally managed?", ('True', 'False'))
managed = 1 if managed_str == 'True' else 0

nights = st.number_input("Minimum stay (nights)", min_value=1, value=2, step=1)

CITIES = ('Asheville', 'Carolina Beach', 'Charlotte', 'Durham', 'Gatlinburg',
          'Myrtle Beach', 'Pigeon Forge', 'Raleigh', 'Williamsburg', 'Wilmington')
city = st.selectbox("City location", CITIES)

if st.button("Predict Revenue"):
    if pipeline is None:
        st.error("Model is not loaded.")
    else:
        # Build dictionary explicitly matching exact model feature names
        input_dict = {
            'photos_count': photo_count,
            'guests': guest_count,
            'bedrooms': bedroom,
            'beds': beds,
            'baths': baths,
            'professional_management': managed,
            'min_nights': nights,
            
            # Start Month dummies (1 through 11; Dec/12 is implicitly all 0s)
            'STARTmonth_1': 1 if selected_month == 1 else 0,
            'STARTmonth_2': 1 if selected_month == 2 else 0,
            'STARTmonth_3': 1 if selected_month == 3 else 0,
            'STARTmonth_4': 1 if selected_month == 4 else 0,
            'STARTmonth_5': 1 if selected_month == 5 else 0,
            'STARTmonth_6': 1 if selected_month == 6 else 0,
            'STARTmonth_7': 1 if selected_month == 7 else 0,
            'STARTmonth_8': 1 if selected_month == 8 else 0,
            'STARTmonth_9': 1 if selected_month == 9 else 0,
            'STARTmonth_10': 1 if selected_month == 10 else 0,
            'STARTmonth_11': 1 if selected_month == 11 else 0,
            
            # Room Type dummies ('entire_home' is implicitly all 0s)
            'room_type_hotel_room': 1 if room_type == 'hotel_room' else 0,
            'room_type_private_room': 1 if room_type == 'private_room' else 0,
            'room_type_unique_location': 1 if room_type == 'unique_location' else 0,
            
            # City dummy
            'City_Gatlinburg': 1 if city == 'Gatlinburg' else 0
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_dict])

        # Verify feature order expected by scaler or pipeline
        try:
            model_features = pipeline.named_steps['scaler'].feature_names_in_
        except AttributeError:
            model_features = getattr(pipeline, "feature_names_in_", input_df.columns)

        # Enforce exact column order
        input_df = input_df.reindex(columns=model_features, fill_value=0)

        # Predict
        try:
            prediction = pipeline.predict(input_df)[0]
            st.success(f"Estimated Monthly Revenue: **${prediction:,.2f}**")
        except Exception as e:
            st.error(f"Prediction error: {e}")
