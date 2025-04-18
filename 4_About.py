import streamlit as st
from utils.styles import set_background, nav_icon

# Set page configuration and background
st.set_page_config(layout="wide")
set_background("assets/background_images/about_bg.jpg")

# Add custom CSS for bright, light-colored text
st.markdown("""
    <style>
    .about-container {
        background: rgba(0, 0, 0, 0.6);
        padding: 40px;
        border-radius: 20px;
        margin-top: 30px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
        max-width: 1000px;
        margin-left: auto;
        margin-right: auto;
        color: #f1f1f1;
    }
    .title-section {
        text-align: center;
        margin-bottom: 40px;
    }
    .title-text {
        font-size: 42px;
        font-weight: bold;
        background: -webkit-linear-gradient(45deg, #00ffff, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
        margin-left: 10px;
    }
    .section-title {
        font-size: 28px;
        color: #00ffff;
        margin-top: 30px;
        border-bottom: 3px solid #00ffff;
        padding-bottom: 6px;
    }
    .section-content {
        font-size: 18px;
        color: #f1f1f1;
        line-height: 1.6;
        margin-top: 10px;
    }
    .highlight {
        color: #ffd700;
        font-weight: 600;
    }
    ul {
        padding-left: 20px;
        color: #f1f1f1;
    }
    ul li {
        margin-bottom: 8px;
    }
    .icon-img {
        width: 45px;
        vertical-align: middle;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Top section: Icon + Gradient Title
st.markdown("""
    <div class="title-section">
        <img src="https://cdn-icons-png.flaticon.com/512/2929/2929662.png" class="icon-img" />
        <span class="title-text">About the Drone Dashboard</span>
    </div>
""", unsafe_allow_html=True)

# Main container
st.markdown("<div class='about-container'>", unsafe_allow_html=True)

# Section: Project Description
st.markdown("<div class='section-title'>🚀 Project Description</div>", unsafe_allow_html=True)
st.markdown("""
<div class="section-content">
This project is a visually enhanced, real-time drone telemetry dashboard built with <span class="highlight">Streamlit</span> and <span class="highlight">Plotly</span>.  
It allows monitoring of key drone metrics including:
<ul>
    <li>🔋 <strong>Battery Voltage</strong></li>
    <li>🎯 <strong>IMU (Roll, Pitch, Yaw)</strong></li>
    <li>🌡️ <strong>Temperature</strong></li>
    <li>🛩️ <strong>Altitude</strong></li>
    <li>📍 <strong>GPS Location</strong></li>
</ul>
The dashboard is crafted for a <span class="highlight">user-friendly and interactive experience</span>, perfect for real-time tracking and visualization.
</div>
""", unsafe_allow_html=True)

# Section: Technologies Used
st.markdown("<div class='section-title'>🧪 Technologies Used</div>", unsafe_allow_html=True)
st.markdown("""
<div class="section-content">
<ul>
    <li>💡 <strong>Streamlit</strong>: Interactive and lightweight Python-based UI framework</li>
    <li>📊 <strong>Plotly</strong>: For dynamic, real-time graphs and gauges</li>
    <li>🐍 <strong>Python</strong>: Backend scripting and telemetry simulation</li>
    <li>🌐 <strong>GitHub</strong>: Collaboration and version control</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Section: Purpose
st.markdown("<div class='section-title'>🎯 Purpose</div>", unsafe_allow_html=True)
st.markdown("""
<div class="section-content">
The goal of this dashboard is to offer an intuitive interface for <span class="highlight">real-time drone monitoring</span>.  
Users can instantly visualize data like battery levels, IMU orientation, location, and more.  
It ensures better operational control, fault detection, and <span class="highlight">live tracking</span> during flight missions.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
