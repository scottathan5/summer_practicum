import streamlit as st
import pandas as pd
import pickle

@st.cache_resource
def load_model():
    try:
        with open("mountainapp.pkl", "rb") as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'mountainapp.pkl' is pushed to your GitHub repository.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

st.title("Mountain AirBnB Profit Predicting App")
st.write("Enter the listing details below:")

# Inputs matching exact categorical training categories
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
selected_month = st.selectbox("Select month to start", MONTHS)

REGION = ('Mountain', 'Piedmont/Central', 'Beach')
selected_region = st.selectbox("Select region to host in", REGION)

TYPE = ('entire_home', 'hotel_room', 'unique_location', 'private_room')
room_type = st.selectbox("Select room type", TYPE)

photo_count = st.number_input("Number of photos you plan to take?", min_value=0, step=1)
guest_count = st.number_input("Number of guests you can accommodate", min_value=0, step=1)
bedroom = st.number_input("Number of bedrooms", min_value=0, step=1)
baths = st.number_input("Number of bathrooms", min_value=0.0, step=0.5)

# Convert selection to boolean to match training data structure
MANAGE = ('True', 'False')
managed_str = st.selectbox("Will it be professionally managed?", MANAGE)
managed = True if managed_str == 'True' else False

nights = st.number_input("Min nights to stay", min_value=0, step=1)

CITIES = ('Asheville', 'Carolina Beach', 'Charlotte', 'Durham', 'Gatlinburg',
          'Myrtle Beach', 'Pigeon Forge', 'Raleigh', 'Williamsburg', 'Wilmington')
city = st.selectbox("What city", CITIES)

# Construct DataFrame using exact feature names used during training
input_data = pd.DataFrame({
    "STARTmonth": [selected_month],
    "region_x": [selected_region],
    "room_type": [room_type],
    "photos_count": [photo_count],
    "guests": [guest_count],
    "bedrooms": [bedroom],
    "beds": [bedroom], # Map default beds if required or update key
    "baths": [baths],
    "professional_management": [managed],
    "min_nights": [nights],
    "City": [city]
})

if st.button("Predict"):
    if model is None:
        st.error("Model is not loaded. Cannot run prediction.")
    else:
        # Perform get_dummies matching training categorical columns
        input_data_encoded = pd.get_dummies(
            input_data, 
            columns=['STARTmonth', 'region_x', 'room_type', 'City'], 
            drop_first=True
        )

        # Align columns with model expectation
        model_columns = getattr(model, "feature_names_in_", [])
        
        if len(model_columns) > 0:
            for col in model_columns:
                if col not in input_data_encoded.columns:
                    input_data_encoded[col] = 0
            
            input_data_encoded = input_data_encoded[model_columns]
            
            try:
                prediction = model.predict(input_data_encoded)[0]
                st.success(f"Estimated Revenue/Profit: **${prediction:,.2f}**")
            except Exception as e:
                st.error(f"Prediction failed: {e}")
        else:
            st.error("Could not retrieve feature names from the loaded model object.")
