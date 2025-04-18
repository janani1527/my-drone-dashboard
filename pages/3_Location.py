import streamlit as st
from utils.styles import set_background
from utils.data_simulation import simulate_telemetry_data

# Set page configuration
st.set_page_config(layout="wide")
set_background("assets/background_images/location_bg.jpg")

# Simulate telemetry data
data = simulate_telemetry_data()

# Display title with minimal, bright colors
st.header("Drone GPS Location")
st.markdown("<h3 style='text-align:center; font-size: 30px; color: #0288d1;'>GPS Coordinates</h3>", unsafe_allow_html=True)

# Add spacing for cleaner layout
st.write("<br>", unsafe_allow_html=True)

# Display GPS information with professional and minimal styling
st.markdown(f"**Latitude**: <span style='font-size: 20px; color: #0288d1;'>{data['gps_lat']}</span>", unsafe_allow_html=True)
st.markdown(f"**Longitude**: <span style='font-size: 20px; color: #0288d1;'>{data['gps_long']}</span>", unsafe_allow_html=True)
st.markdown(f"**Altitude**: <span style='font-size: 20px; color: #0288d1;'>{data['gps_alt']} meters</span>", unsafe_allow_html=True)

# Optional: You can also display GPS accuracy if available
st.markdown(f"**GPS Accuracy**: <span style='font-size: 20px; color: #0288d1;'>{data.get('gps_accuracy', 'N/A')} meters</span>", unsafe_allow_html=True)

# Show the map centered on the drone's latitude and longitude
st.map({
    "lat": [data["gps_lat"]],
    "lon": [data["gps_long"]]
})

# Add spacing for cleaner layout
st.write("<br>", unsafe_allow_html=True)
