import streamlit as st
from utils.styles import set_background,nav_icon

# Set page config and background
st.set_page_config(layout="wide")
set_background("assets/background_images/telemetry_bg.jpg")

# Title with styling
st.markdown("""
    <h1 style='text-align: center; color: #ffffff;'>DRONE MONITORING DASHBOARD</h1>
    <hr style="border: 1px solid #444;">
""", unsafe_allow_html=True)

# Title and styling for the page with the background from assets
st.markdown("""
    <style>
    

    

    .sub-greet {
        font-size: 20px;
        color: #f2f2f2;
        text-align: center;
        margin-bottom: 20px;
        font-weight: 400;
    }

    .description {
        font-size: 18px;
        color: #ffffff;
        text-align: center;
        margin-top: 20px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Main content: Title and Greeting
st.markdown("""
    
    <p class="sub-greet">Hello Pilots! Ready for takeoff? 🛸</p>
    
    <div class="description">
        <p>⚡ Live Battery Voltage</p>
        <p>📡 IMU: Roll, Pitch, Yaw</p>
        <p>🌡️ Temperature & Altitude</p>
        <p>🛰️ GPS Location & Trails</p>
        <p>🔔 Real-Time Alerts</p>
        <p>Explore the dashboard to monitor your drone's health and performance!</p>
    </div>
""", unsafe_allow_html=True)
