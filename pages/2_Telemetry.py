import streamlit as st
from utils.styles import set_background, nav_icon
from utils.data_simulation import simulate_telemetry_data
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import random

# Set page config and background
st.set_page_config(layout="wide")
set_background("assets/background_images/telemetry_bg.jpg")

# Title with styling
st.markdown("""
    <h1 style='text-align: center; color: #ffffff;'>Drone Telemetry Dashboard</h1>
    <hr style="border: 1px solid #444;">
""", unsafe_allow_html=True)

# Simulate telemetry data
data = simulate_telemetry_data()

# Helper to generate small random graph data
def generate_graph_data(label, value, noise_range=0.3):
    return pd.DataFrame({
        "Time": pd.date_range(end=pd.Timestamp.now(), periods=10, freq="S"),
        label: [round(value + random.uniform(-noise_range, noise_range), 2) for _ in range(10)]
    })

# === Battery Voltage ===
st.markdown("<h3 style='color:#00ffff;'>🔋 Battery Voltage (V)</h3>", unsafe_allow_html=True)
st.metric(label="Battery Voltage", value=f"{data['battery_voltage']} V")
st.line_chart(generate_graph_data("Voltage", data["battery_voltage"]).set_index("Time"))
st.markdown("<br><br>", unsafe_allow_html=True)

# === Temperature ===
st.markdown("<h3 style='color:#ff6666;'>🌡️ Temperature (°C)</h3>", unsafe_allow_html=True)
st.metric(label="Temperature", value=f"{data['temperature']} °C")
st.line_chart(generate_graph_data("Temperature", data["temperature"]).set_index("Time"))
st.markdown("<br><br>", unsafe_allow_html=True)

# === Roll Gauge ===
st.markdown("<h3 style='color:#66ccff;'>🎚️ Roll (°)</h3>", unsafe_allow_html=True)
fig_roll = go.Figure(go.Indicator(
    mode="gauge+number",
    value=data["imu_roll"],
    title={'text': "Roll", 'font': {'size': 28}},
    gauge={
        'axis': {'range': [-180, 180]},
        'bar': {'color': "royalblue"},
        'bgcolor': "white"
    }
))
fig_roll.update_layout(height=350, margin=dict(l=40, r=40, t=70, b=40))
st.plotly_chart(fig_roll, use_container_width=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# === Pitch Gauge ===
st.markdown("<h3 style='color:#ff9933;'>📐 Pitch (°)</h3>", unsafe_allow_html=True)
fig_pitch = go.Figure(go.Indicator(
    mode="gauge+number",
    value=data["imu_pitch"],
    title={'text': "Pitch", 'font': {'size': 28}},
    gauge={
        'axis': {'range': [-90, 90]},
        'bar': {'color': "orange"},
        'bgcolor': "white"
    }
))
fig_pitch.update_layout(height=350, margin=dict(l=40, r=40, t=70, b=40))
st.plotly_chart(fig_pitch, use_container_width=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# === Altitude ===
st.markdown("<h3 style='color:#00cc66;'>🛫 Altitude (m)</h3>", unsafe_allow_html=True)
st.metric(label="Altitude", value=f"{data['altitude']} m")
st.line_chart(generate_graph_data("Altitude", data["altitude"]).set_index("Time"))
st.markdown("<br><br>", unsafe_allow_html=True)

# Yaw Gauge Section
st.divider()

st.markdown("<h3 style='color:#cc66ff;'>🧭 Yaw (°)</h3>", unsafe_allow_html=True)
fig_yaw = go.Figure(go.Indicator(
    mode="gauge+number",
    value=data["imu_yaw"],  # Yaw value from your telemetry data
    title={'text': "Yaw", 'font': {'size': 24}},  # Title font size
    gauge={
        'axis': {'range': [-180, 180]},  # Range for yaw
        'bar': {'color': "#cc66ff"},  # Color for the gauge bar
        'bgcolor': "white",  # Background color for the gauge
        'steps': [
            {'range': [-180, -90], 'color': '#ff9999'},  # Optional: red section for -180 to -90 range
            {'range': [-90, 0], 'color': '#ffcc66'},  # Yellow section for -90 to 0 range
            {'range': [0, 90], 'color': '#99ff99'},  # Green section for 0 to 90 range
            {'range': [90, 180], 'color': '#66ccff'}  # Blue section for 90 to 180 range
        ],
    }
))

# Update layout for the gauge and make sure everything is visible
fig_yaw.update_layout(
    height=320,  # Gauge height
    margin=dict(l=20, r=20, t=60, b=0)  # Adjust margins for proper spacing
)

# Display the gauge with full container width
st.plotly_chart(fig_yaw, use_container_width=True)


# Optional spacing at bottom
st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
