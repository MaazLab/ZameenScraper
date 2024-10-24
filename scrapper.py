from bs4 import BeautifulSoup
import os

BASE_URL = 'https://www.zameen.com/'

# GET REQUEST  
def request_server(url):
    pass

def city_mapping(city):
    
    city_mapper = { 'Islamabad': 'Islamabad-3-', 'Karachi': 'Karachi-2-', 'Lahore': 'Lahore-1-', 'Rawalpindi': 'Rawalpindi-41-', 'Abbottabad': 'Abbottabad-385-', 
                'Abdul Hakim': 'Abdul_Hakim-10594-', 'Ahmedpur East': 'Ahmedpur_East-12360-', 'Ali Masjid': 'Ali_Masjid-18624-', 'Alipur': 'Alipur-10242-', 'Arifwala': 'Arifwala-9517-',
                'Astore': 'Astore-1763-', 'Attock': 'Attock-1233-', 'Awaran': 'Awaran-1761-', 'Badin': 'Badin-8857-', 'Bagh': 'Bagh-966-', 'Bahawalnagar': 'Bahawalnagar-557-',
                'Bahawalpur': 'Bahawalpur-23-', 'Balakot':'Balakot-14226-', 'Bannu': 'Bannu-1735-', 'Barnala': 'Barnala-13977-', 'Batkhela': 'Batkhela-13808-', 
                'Battagram': 'Battagram-17727-', 'Bhakkar': 'Bhakkar-1720-', 'Bhalwal': 'Bhalwal-11142-', 'Bhimber': 'Bhimber-1749-','Buner': 'Buner-11286-', 'Burewala': 'Burewala-1059-', 
                'Chaghi': 'Chaghi-1747-', 'Chakwal': 'Chakwal-751-', 'Charsadda': 'Charsadda-11420-', 'Chichawatni': 'Chichawatni-8860-', 'Chilas': 'Chilas-17728-', 
                'Chiniot': 'Chiniot-1469-', 'Chishtian': 'Chishtian-17729-', 'Chishtian Sharif': 'Chishtian_Sharif-10512-', 'Chitral': 'Chitral-1731-', 'Choa Saidan Shah': 'Choa_Saidan_Shah-14284-', 
                'Chunian': 'Chunian-1061-', 'Dadu': 'Dadu-1727-', 'Daharki': 'Daharki-11967-', 'Daska': 'Daska-1509-', 'Daur': 'Daur-13599-', 'Depalpur': 'Depalpur-9178-', 
                'Dera Ghazi Khan': 'Dera_Ghazi_Khan-26-', 'Dera Ismail Khan': 'Dera_Ismail_Khan-8244-', 'Dijkot': 'Dijkot-10645-', 'Dina': 'Dina-12718-', 'Dinga': 'Dinga-2-',
                'Dobian': 'Dobian-14195-', 'Duniya Pur': 'Duniya_Pur-8474-','FATA': 'FATA-1737-', 'Faisalabad': 'Faisalabad-16-', 'Fateh Jang': 'Fateh_Jang-1293-', 
                'Gaddani': 'Gaddani-19047-', 'Gadoon': 'Gadoon-11915-', 'Galyat': 'Galyat-8119-', 'Gambat': 'Gambat-18016-', 'Ghakhar': 'Ghakhar-13272-', 'Ghanche': 'Ghanche-17730-',
                'Gharo': 'Gharo-636-', 'Ghizar': 'Ghizar-17768-', 'Ghotki': 'Ghotki-8810-', 'Gilgit': 'Gilgit-1753-', 'Gojra': 'Gojra-10281-', 'Gujar Khan': 'Gujar_Khan-8338-',
                'Gujranwala': 'Gujranwala-327-', 'Gujrat': 'Gujrat-20-', 'Gwadar': 'Gwadar-389-', 'Hafizabad': 'Hafizabad-1714-', 'Hala': 'Hala-13607-', 'Hangu': 'Hangu-11739-',
                'Harappa': 'Harappa-11634-', 'Haripur': 'Haripur-1048-', 'Haroonabad': 'Haroonabad-1152-', 'Hasilpur': 'Hasilpur-9687-', 'Hassan Abdal': 'Hassan_Abdal-399-', 'Haveli Lakha': 'Haveli_Lakha-10402-', 'Hazro': 'Hazro-12823-',
                'Hub Chowki': 'Hub_Chowki-9844-', 'Hujra Shah Muqeem': 'Hujra_Shah_Muqeem-13569-', 'Hunza': 'Hunza-1546-', 'Hyderabad': 'Hyderabad-30-', 'Jacobabad': 'Jacobabad-32-', 'Jahanian': 'Jahanian-11126-', 
                'Jalalpur Jattan': 'Jalalpur_Jattan-11026-', 'Jampur': 'Jampur-10484-', 'Jamshoro': 'Jamshoro-1178-', 'Jandola': 'Jandola-17731-', 'Jaranwala': 'Faisalabad_Jaranwala-1363-', 'Jatoi': 'Jatoi-13706-',
                'Jauharabad': 'Jauharabad-8511-', 'Jhang': 'Jhang-1142-', 'Jhelum': 'Jhelum-19-', 'Kabirwala': 'Kabirwala-9873-', 'Kaghan': 'Kaghan-9202-', 'Kahror Pakka': 'Kahror_Pakka-10279-', 'Kalat': 'Kalat-1750-',
                'Kamalia': 'Kamalia-10416-', 'Kamoki': 'Kamoki-10346-', 'Kandiaro': 'Kandiaro-13611-', 'Karak': 'Karak-9484-', 'Kasur': 'Kasur-544-', 'Khairpur': 'Khairpur-8806-', 'Khanewal': 'Khanewal-1685-',
                'Khanpur': 'Khanpur-10168-', 'Khaplu': 'Khaplu-17732-', 'Kharian': 'Kharian-1305-', 'Khipro': 'Khipro-12390-', 'Khushab': 'Khushab-8510-', 'Khuzdar': 'Khuzdar-1757-', 'Kohat': 'Kohat-1430-', 
                'Kohistan': 'Kohistan-17733-', 'Kot Addu': 'Kot_Addu-9749-', 'Kotli': 'Kotli-968-', 'Kotri': 'Kotri-8591-', 'Lakki Marwat': 'Lakki_Marwat-10205-', 'Lalamusa': 'Lalamusa-9837-',
                'Landi Kotal': 'Landi_Kotal-17734-', 'Larkana': 'Larkana-586-', 'Lasbela': 'Lasbela-548-', 'Layyah': 'Layyah-1661-', 'Liaquatpur': 'Liaquatpur-11406-', 'Lodhran': 'Lodhran-9872-',
                'Loralai': 'Loralai-1742-', 'Lower Dir': 'Lower_Dir-10482-', 'Mailsi': 'Mailsi-9422-', 'Makran': 'Makran-1767-', 'Malakand': 'Malakand-1384-', 'Malal': 'Fateh_Jang_Malal-21681-',
                'Mandi Bahauddin': 'Mandi_Bahauddin-1496-', 'Mangla': 'Mangla-14350-', 'Mansehra': 'Mansehra-771-', 'Mardan': 'Mardan-440-', 'Matiari': 'Matiari-8606-', 'Matli': 'Matli-14120-', 
                'Mehrabpur': 'Mehrabpur-2-', 'Mian Channu': 'Mian_Channu-9636-', 'Mianwali': 'Mianwali-8310-', 'Mingora': 'Mingora-13476-', 'Miran Shah': 'Miran_Shah-17735-', 'Mirpur': 'Mirpur-1349-',
                'Mirpur Khas': 'Mirpur_Khas-1558-', 'Mirpur Sakro': 'Mirpur_Sakro-10893-', 'Mitha Tiwana': 'Mitha_Tiwana-13421-', 'Moro': 'Moro-13603-', 'Multan': 'Multan-15-', 'Muridke': 'Muridke-8116-',
                'Murree': 'Murree-36-', 'Muzaffarabad': 'Muzaffarabad-977-', 'Muzaffargarh': 'Muzaffargarh-1722-', 'Nankana Sahib': 'Nankana_Sahib_-1687-', 'Naran': 'Naran-1258-', 'Narowal': 'Narowal-541-', 
                'Nasirabad': 'Nasirabad-1752-', 'Naushahro Feroze': 'Naushahro_Feroze-8801-', 'Nawabshah': 'Nawabshah-1704-', 'Neelum': 'Neelum-1741-', 'Nowshera': 'Nowshera-1424-', 'Okara': 'Okara-470-',
                'Pakpattan': 'Pakpattan-1716-', 'Pallandri': 'Pallandri-17736-', 'Parachinar': 'Parachinar-17737-', 'Pasrur': 'Pasrur-17168-', 'Pattoki': 'Pattoki-8197-', 'Peshawar': 'Peshawar-17-', 
                'Pind Dadan Khan': 'Pind_Dadan_Khan-10678-', 'Pindi Bhattian': 'Pindi_Bhattian-975-', 'Pir Mahal': 'Pir_Mahal-9508-', 'Poonch': 'Poonch-17711-', 'Qazi Ahmed': 'Qazi_Ahmed-13617-', 'Quetta': 'Quetta-18-',
                'Rahim Yar Khan': 'Rahim_Yar_Khan-40-', 'Raiwind': 'Raiwind-17707-', 'Rajanpur': 'Rajanpur-9645-', 'Rato Dero': 'Rato_Dero-17738-', 'Rawalakot': 'Rawalakot-976-',
                'Renala Khurd': 'Renala_Khurd-8151-', 'Rohri': 'Rohri-1725-', 'Sadiqabad': 'Sadiqabad-9538-', 'Sahiwal': 'Sahiwal-782-', 'Sakrand': 'Sakrand-13438-', 'Samundri': 'Samundri-10632-',
                'Sanghar': 'Sanghar-8609-', 'Sangla Hill': 'Sangla_Hill-8563-', 'Sarai Alamgir': 'Sarai_Alamgir-1034-', 'Sargodha': 'Sargodha-778-', 'Sehwan': 'Sehwan-8607-',
                'Shabqadar': 'Shabqadar-13211-', 'Shahdadpur': 'Shahdadpur-9029-', 'Shahkot': 'Shahkot-8552-', 'Shahpur Chakar': 'Shahpur_Chakar-13614-', 'Shakargarh': 'Shakargarh-12170-',
                'Shangla': 'Shangla-17739-', 'Shehr Sultan': 'Shehr_Sultan-13703-', 'Sheikhupura': 'Sheikhupura-44-', 'Sher Garh': 'Sher_Garh-13570-', 'Shikarpur': 'Shikarpur-8808-', 
                'Shorkot': 'Shorkot-10334-', 'Sialkot': 'Sialkot-480-', 'Sibi': 'Sibi-1744-', 'Skardu': 'Skardu-1545-', 'Sudhnoti': 'Sudhnoti-1745-', 'Sujawal': 'Sujawal-14329-', 
                'Sukkur': 'Sukkur-45-', 'Swabi': 'Swabi-3094-', 'Swat': 'Swat-1506-', 'Talagang': 'Talagang-12137-', 'Tando Adam': 'Tando_Adam-9028-', 'Tando Allahyar': 'Tando_Allahyar-11315-', 
                'Tando Bago': 'Tando_Bago-11700-', 'Tando Muhammad Khan': 'Tando_Muhammad_Khan-13166-', 'Tank': 'Tank-17740-', 'Taxila': 'Taxila-464-', 'Tharparkar': 'Tharparkar-12439-',
                'Thatta': 'Thatta-1729-', 'Toba Tek Singh': 'Toba_Tek_Singh-1658-', 'Torkham': 'Torkham-17741-', 'Turbat': 'Turbat-12271-', 'Umarkot': 'Umarkot-17742-', 'Upper Dir': 'Upper_Dir-17743-', 
                'Vehari': 'Vehari-1432-', 'Wah': 'Wah-459-', 'Wana': 'Wana-17744-', 'Wazirabad': 'Wazirabad-1395-', 'Waziristan': 'Waziristan-1765-', 'Yazman': 'Yazman-12504-', 'Zhob': 'Zhob-1739-'}
    return city_mapper[city]

# Main Scrapping process
def scrape(purpose, city, price_range, area_range, beds, baths ):

    price_min , price_max = price_range
    area_min, area_max = area_range

    filters = f'?price_min={price_min}&price_max={price_max}&area_min={area_min*20.903184}&area_max={area_max*20.903184}'

    if 'All' in beds:
        pass
    else:
        beds = '&beds_in='+'%2C'.join(beds).replace('+','%2B').replace('Studio','0')
        filters+= beds
        print(beds)
    
    if 'All' in baths:
        pass
    else:
        baths = '&baths_in='+'%2C'.join(baths).replace('+','%2B')
        filters+= baths
        print(baths)
    
    purpose = 'Homes' if purpose == "BUY" else 'Rentals'
    city = city_mapping(city)

    for i in range(1,10):
        url = BASE_URL+f'/{purpose}/{city}{i}.html{filters}'
        return url