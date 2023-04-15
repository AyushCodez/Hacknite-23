from bs4 import BeautifulSoup
import requests

def get_details(URL):
	HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)', 'Accept-Language': 'en-US, en;q=0.5'})

	webpage = requests.get(URL, headers=HEADERS)
	soup = BeautifulSoup(webpage.content, 'lxml')
	
	try:
		title = soup.find('span', attrs={'id': 'productTitle'})
		title_string = title.string.strip().replace(',', '')
	except AttributeError:
		title_string = 'NA'

	try:
		price = soup.find('span', attrs={'class': 'a-price-whole'}).text.strip().replace('₹', '').rstrip('.')
	except AttributeError:
		price = 'NA'

	try:
		rating = soup.find('i', attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')
	except AttributeError:
		try:
			rating = soup.find('span', attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
		except:
			rating = 'NA'
			
	try:
		img = soup.find('img', {'class': 'a-dynamic-image'})
		image = img['src'].strip()
	except:
		image = ''
	
	return (title_string, image, price, rating)