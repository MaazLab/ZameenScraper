import streamlit as st
import base64
import os
import scrapper

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
st.sidebar.header("Input Parameters")

# Radio button for Buy/Sell selection
transaction_type = st.sidebar.radio("Transaction Type", ["BUY", "RENT"])

# Create the form inside the sidebar
city = st.sidebar.selectbox('City', ['Islamabad', 'Karachi', 'Lahore', 'Rawalpindi', 'Abbottabad', 'Abdul Hakim', 'Ahmedpur East', 'Ali Masjid', 'Alipur', 'Arifwala', 'Astore', 'Attock','Awaran', 'Badin', 'Bagh', 
                                     'Bahawalnagar', 'Bahawalpur', 'Balakot', 'Bannu', 'Barnala', 'Batkhela', 'Battagram', 'Bhakkar', 'Bhalwal', 'Bhimber','Buner', 'Burewala', 'Chaghi', 'Chakwal', 'Charsadda',
                                     'Chichawatni', 'Chilas', 'Chiniot', 'Chishtian', 'Chishtian Sharif', 'Chitral', 'Choa Saidan Shah','Chunian', 'Dadu', 'Daharki', 'Daska', 'Daur', 'Depalpur', 'Dera Ghazi Khan',
                                     'Dera Ismail Khan', 'Dijkot', 'Dina', 'Dinga', 'Dobian', 'Duniya Pur', 'FATA', 'Faisalabad', 'Fateh Jang', 'Gaddani', 'Gadoon', 'Galyat', 'Gambat', 'Ghakhar', 'Ghanche', 'Gharo',
                                     'Ghizar', 'Ghotki', 'Gilgit', 'Gojra', 'Gujar Khan','Gujranwala', 'Gujrat', 'Gwadar', 'Hafizabad', 'Hala', 'Hangu', 'Harappa', 'Haripur', 'Haroonabad', 'Hasilpur', 'Hassan Abdal',
                                     'Haveli Lakha', 'Hazro', 'Hub Chowki', 'Hujra Shah Muqeem', 'Hunza', 'Hyderabad', 'Jacobabad', 'Jahanian', 'Jalalpur Jattan', 'Jampur', 'Jamshoro', 'Jandola', 'Jaranwala', 'Jatoi',
                                     'Jauharabad', 'Jhang', 'Jhelum', 'Kabirwala', 'Kaghan', 'Kahror Pakka', 'Kalat', 'Kamalia', 'Kamoki', 'Kandiaro', 'Karak', 'Kasur', 'Khairpur', 'Khanewal',
                                     'Khanpur', 'Khaplu', 'Kharian', 'Khipro', 'Khushab', 'Khuzdar', 'Kohat', 'Kohistan', 'Kot Addu', 'Kotli', 'Kotri', 'Lakki Marwat', 'Lalamusa', 'Landi Kotal',
                                     'Larkana', 'Lasbela', 'Layyah', 'Liaquatpur', 'Lodhran', 'Loralai', 'Lower Dir', 'Mailsi', 'Makran', 'Malakand', 'Malal', 'Mandi Bahauddin', 'Mangla', 'Mansehra',
                                     'Mardan', 'Matiari', 'Matli', 'Mehrabpur', 'Mian Channu', 'Mianwali', 'Mingora', 'Miran Shah', 'Mirpur', 'Mirpur Khas', 'Mirpur Sakro', 'Mitha Tiwana', 'Moro',
                                     'Multan', 'Muridke', 'Murree', 'Muzaffarabad', 'Muzaffargarh', 'Nankana Sahib', 'Naran', 'Narowal', 'Nasirabad', 'Naushahro Feroze', 'Nawabshah', 'Neelum', 'Nowshera',
                                     'Okara', 'Pakpattan', 'Pallandri', 'Parachinar', 'Pasrur', 'Pattoki', 'Peshawar', 'Pind Dadan Khan', 'Pindi Bhattian', 'Pir Mahal', 'Poonch', 'Qazi Ahmed', 'Quetta',
                                     'Rahim Yar Khan', 'Raiwind', 'Rajanpur', 'Rato Dero', 'Rawalakot', 'Renala Khurd', 'Rohri', 'Sadiqabad', 'Sahiwal', 'Sakrand', 'Samundri', 'Sanghar', 'Sangla Hill',
                                     'Sarai Alamgir', 'Sargodha', 'Sehwan', 'Shabqadar', 'Shahdadpur', 'Shahkot', 'Shahpur Chakar', 'Shakargarh', 'Shangla', 'Shehr Sultan', 'Sheikhupura', 'Sher Garh',
                                     'Shikarpur', 'Shorkot', 'Sialkot', 'Sibi', 'Skardu', 'Sudhnoti', 'Sujawal', 'Sukkur', 'Swabi', 'Swat', 'Talagang', 'Tando Adam', 'Tando Allahyar', 'Tando Bago',
                                     'Tando Muhammad Khan', 'Tank', 'Taxila', 'Tharparkar', 'Thatta', 'Toba Tek Singh', 'Torkham', 'Turbat', 'Umarkot', 'Upper Dir', 'Vehari', 'Wah', 'Wana', 'Wazirabad',
                                     'Waziristan', 'Yazman', 'Zhob'])
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
    st.write(f'Location: {location}\t TYPE {type(location)}')
    st.write(f'Property Type: {property_type}')
    st.write(f'Price Range: {price_range}')
    st.write(f'Area: {area}')
    st.write(f'Beds: {beds}')
    st.write(f'transaction_type: {transaction_type}')
    st.write(scrapper.scrape(transaction_type=transaction_type, city=city ))