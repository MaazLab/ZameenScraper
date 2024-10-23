from bs4 import BeautifulSoup
import os

base_url = 'https://www.zameen.com/'

# GET REQUEST  
def request_server(url):
    pass

# Main Scrapping process
def scrape(transaction_type, city ):

    # URL setting a/c to transaction type
    url = os.path.join(base_url,'Homes') if transaction_type == "BUY" else os.path.join(base_url,'Rentals')
    
    url = url+f'/{city}-1-1.html'
    return url