
import streamlit as st
import joblib
import pandas as pd

st.title("Bus Passenger Demand - Demo App")
st.write("Project: Bus Passenger Demand (Dar es Salaam context)")

model = joblib.load("model.pkl")

# User inputs
hour = st.number_input("Hour of day (0-23)", min_value=0, max_value=23, value=8)
is_weekend = st.selectbox("Is Weekend?", ("No","Yes"))
is_weekend = 1 if is_weekend=="Yes" else 0
route = st.selectbox("Route", ["Mbezi-Kariakoo","Tegeta-Posta","Kimara-Kivukoni","Ubungo-Kivukoni"])
weather = st.selectbox("Weather", ["Sunny","Cloudy","Rainy"])
temperature = st.number_input("Temperature (°C)", value=28)

input_df = pd.DataFrame([{'Hour':hour,'Is_Weekend':is_weekend,'Route':route,'Weather':weather,'Temperature':temperature}])

if st.button("Predict"):
    pred = model.predict(input_df)[0]
    st.success(f"Predicted passenger count: {int(round(pred))}")
