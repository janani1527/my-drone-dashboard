import streamlit as st
import base64

def set_background(image_path):
    ext = image_path.split('.')[-1]
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/{ext};base64,{encoded}"); 
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        .block-container {{
            padding-top: 2rem;
            padding-bottom: 0rem;
        }}
        .nav-icon-container {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .nav-icon-container img {{
            border-radius: 12px;
            transition: transform 0.2s ease;
        }}
        .nav-icon-container img:hover {{
            transform: scale(1.1);
        }}
        </style>
        """, unsafe_allow_html=True
    )

def nav_icon(icon_path, target_page):
    # Read the image file
    with open(icon_path, "rb") as f:
        icon_b64 = base64.b64encode(f.read()).decode()
    
    # Display the icon image with a smaller width
    if st.button(
        f'<img src="data:image/webp;base64,{icon_b64}" width="100" />',
        key=target_page,
        help=f"Go to {target_page}",
    ):
        # Update the session state to switch the page
        st.session_state.page = target_page
