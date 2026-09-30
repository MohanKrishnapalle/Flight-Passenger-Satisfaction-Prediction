import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Flight Passenger Satisfaction Predictor", page_icon="✈️")
st.title("Flight Passenger Satisfaction Predictor")

# Load model and target encoder
@st.cache_resource
def load_model():
    model = joblib.load("rf_pipeline.joblib")
    target_encoder = joblib.load("label_encoder_target.joblib")
    return model, target_encoder

model, target_encoder = load_model()

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
customer_type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
travel_type = st.selectbox("Type of Travel", ["Business travel", "Personal Travel"])
travel_class = st.selectbox("Class", ["Business", "Eco", "Eco Plus"])

age = st.slider("Age", 0, 100, 30)
flight_distance = st.slider("Flight Distance", 0, 5000, 1000)
dep_delay = st.slider("Departure Delay (min)", 0, 1000, 0)
arr_delay = st.slider("Arrival Delay (min)", 0, 1000, 0)

# Service ratings
ratings = {}
services = [
    "Inflight wifi service", "Departure/Arrival time convenient", "Ease of Online booking",
    "Gate location", "Food and drink", "Online boarding", "Seat comfort", "Inflight entertainment",
    "On-board service", "Leg room service", "Baggage handling", "Checkin service",
    "Inflight service", "Cleanliness"
]
for service in services:
    ratings[service] = st.slider(service, 0, 5, 3)

# Build input DataFrame
input_data = pd.DataFrame([{
    "Gender": gender,
    "Customer Type": customer_type,
    "Age": age,
    "Type of Travel": travel_type,
    "Class": travel_class,
    "Flight Distance": flight_distance,
    "Departure Delay in Minutes": dep_delay,
    "Arrival Delay in Minutes": arr_delay,
    **ratings
}])

# Predict
if st.button("Predict Satisfaction"):
    pred_encoded = model.predict(input_data)[0]
    pred_label = target_encoder.inverse_transform([pred_encoded])[0]

    if "dissatisfied" in pred_label.lower():
        st.error(f"Prediction: {pred_label}")
    elif "neutral" in pred_label.lower():
        st.warning(f"Prediction: {pred_label}")
    else:
        st.success(f"Prediction: {pred_label}")
