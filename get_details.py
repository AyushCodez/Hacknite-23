from bs4 import BeautifulSoup
import requests
from time import time

def get_details(URL):
    HEADERS = ({'User-Agent':'Chrome/44.0.2403.159', 'Accept-Language': 'en-US, en;q=0.5'})
    print('1')
    ms_before = int(time()*1000)
    webpage = requests.get(url=URL, headers=HEADERS)
    ms_now = int(time()*1000)
    print(ms_now-ms_before,'ms')
    soup = BeautifulSoup(webpage.content, 'lxml')

    try:
        title = soup.find('span', attrs={'id': 'productTitle'}).text.strip().replace(',', '')
    except AttributeError:
        title = 'NA'

    try:
        price = soup.find('span', attrs={'class': 'a-price-whole'}).text.strip().replace('₹', '').rstrip('.')
    except AttributeError:
        price = 'NA'

    try:
        rating = soup.find('i', attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')
    except AttributeError:
        rating = 'NA'
            
    try:
        img = soup.find('img', {'class': 'a-dynamic-image'})
        image = img['src'].strip()
    except:
        image = ''

    return (title, image, price, rating)