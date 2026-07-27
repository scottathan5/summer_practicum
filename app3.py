import streamlit as st
import numpy as np
import pandas as pd
import pickle

def load_model():
    try:
        with open("mountainapp.pkl", "rb") as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'iris_model.pkl' is in the same directory.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

st.title("Mountain airBNB profit predicting app")
st.write("Enter the listing shizz")

# Input fields
# ['revenue', 'STARTmonth','region_x','room_type','photos_count','guests','bedrooms','beds','baths','professional_management','min_nights', 'City']
# pd.get_dummies(front_mountains, columns=['STARTmonth','region_x','room_type','City'], drop_first=True)

# Month selector
# Month names
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December')
selected_month = st.selectbox("Select month to start", MONTHS)

# region selector
REGION = ('Mountain','Piedmont/Central','Beach')
selected_region = st.selectbox("Select region to host in", REGION)


# room type
TYPE = ('entire_home', 'hotel_room', 'unique_location', 'private_room')
room_type = st.selectbox("Select room type", TYPE)


# photo count
photo_count = st.number_input("Number of photos you plan to take?", min_value=0.0, step=1)


# guest count
guest_count = st.number_input("Number of guests you can accomodate", min_value=0.0, step=1)


#bedrooms
bedroom = st.number_input("Number of bedrooms", min_value=0.0, step=1)

# baths
baths = st.number_input("Number of bathrooms", min_value=0.0, step=0.5)


#managed?
MANAGE = ('True','False')
managed = st.selectbox("Will it be professionally managed?", MANAGE)


#nights
nights = st.number_input("Min nights to stay", min_value=0.0, step=1)

# city
CITIES = ('Asheville', 'Carolina Beach', 'Charlotte', 'Durham', 'Gatlinburg',
       'Myrtle Beach', 'Pigeon Forge', 'Raleigh', 'Williamsburg',
       'Wilmington')
city = st.selectbox("What city", CITIES)


input_data = pd.DataFrame({
    "Month": [selected_month],
    "Region": [selected_region],
    "Room type": [room_type],
    "Photo count": [photo_count],
    "Guest count": [guest_count],
    "# bedrooms": [bedroom],
    "baths": [baths],
    "Professionally managed?": [managed],
    "min nights": [nights],
    "city": [city]
})

input_data_encoded = pd.get_dummies(input_data, columns=['Month','Region','Room type','Professionally managed?','city'])

model_columns = model.feature_names_in_
for col in model_columns:
    if col not in input_data_encoded.columns:
        input_data_encoded[col] = 0

input_data_encoded = input_data_encoded[model_columns]


if st.button("Predict"):
    prediction = model.predict(input_data_encoded)[0]

