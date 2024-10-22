import streamlit as st
import base64
import os

# Initialize paths
base_path = os.getcwd()
images_path = os.path.join(base_path,'images')

# logos path
sidebar_logo = os.path.join(images_path,'sidebar_logo.jpeg')
main_body_logo = os.path.join(images_path, "body_logo.png")
st.logo(sidebar_logo, icon_image=main_body_logo)

# Function to encode image to base64 for background image
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to the background image
background_image_path = os.path.join(images_path,'background.webp')  # Replace with your image file path
base64_image = get_base64_image(background_image_path)

# Custom CSS with the background image
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{base64_image}"); 
        background-size: cover;
        background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)

# Sidebar for input parameters
st.sidebar.header("Input Parameters for Scraper")

# Create the form inside the sidebar
city = st.sidebar.selectbox('City', ['Lahore', 'Karachi', 'Islamabad'])
location = st.sidebar.text_input('Location')
property_type = st.sidebar.selectbox('Property Type', ['Homes', 'Plots', 'Commercial'])
price_range = st.sidebar.slider('Price (PKR)', 0, 100000000, (0, 5000000))
area = st.sidebar.slider('Area (Marla)', 0, 100, (0, 10))
beds = st.sidebar.selectbox('Beds', ['All', '1', '2', '3', '4', '5+'])

# Button to submit the form
submit_button = st.sidebar.button(label='Scrape')

# If the button is pressed
if submit_button:
    st.write(f'Searching for properties in {city}...')
    st.write(f'Location: {location}')
    st.write(f'Property Type: {property_type}')
    st.write(f'Price Range: {price_range}')
    st.write(f'Area: {area}')
    st.write(f'Beds: {beds}')
