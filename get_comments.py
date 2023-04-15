# importing libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
driver = webdriver.Chrome()

def main(URL):
    HEADERS = ({'User-Agent':'Chrome/44.0.2403.157','Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    driver.get(URL)
    r = driver.page_source


    soup = BeautifulSoup(r, "lxml")

    with open("temp.html","w",encoding="utf-8") as f:
        f.write(str(soup))
	
    para = soup.find_all('a', attrs = {'data-reftag':"cm_cr_othr_d_lh_1"}) 

    print(para)




if __name__ == '__main__':
    links = ["https://www.amazon.in/Xbox-Wireless-Controller-Carbon-Black/dp/B08K3FVP5N/"]
    for link in links:
        main(link)
