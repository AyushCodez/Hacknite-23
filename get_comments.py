# importing libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import time
class Data:

    def __init__(self, link, name, image, price, rating):
        self.link, self.name, self.image, self.price, self.rating = link, name, image, price, rating
        if (len(self.name) >= 40):
            self.name = self.name[0:38]+'...'
    
    def __repr__(self) -> str:
        string = f"""Link: {self.link}
        Name: {self.name}
        Image: {self.image}
        Price: {self.price}
        Rating: {self.rating}"""

        return string

def get_keywords(URL):

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    options = webdriver.ChromeOptions() 
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver.get(URL)
    time.sleep(1)
    element = driver.find_element(By.CLASS_NAME,"cr-widget-TitleRatingsHistogram")

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    a = driver.find_elements(By.CLASS_NAME,"a-declarative")

    r = driver.page_source

    soup = BeautifulSoup(r, "html.parser")
	
    para = soup.find_all('span', attrs = {"data-action":"reviews:filter-action:apply"})
    
    for i in para:
        print(i.text.strip())

    driver.quit()

def get_links(keyword: str):
    
    keyword = keyword.replace(" ", "+")
    HEADERS = ({'User-Agent':'Chrome/44.0.2403.159', 'Accept-Language': 'en-US, en;q=0.5'})
    r = requests.get(f"https://www.amazon.in/s?k={keyword}", headers=HEADERS)

    soup = BeautifulSoup(r.content,"html.parser")

    with open("temp.html","w",encoding="utf-8") as f:
        f.write(str(soup))
	

    elem = soup.find_all('div', attrs= {"data-component-type":"s-search-result"})

    data = []
    for i in elem:
        try:
            temp = i.find('a')
            t = temp["href"]
            while "bestsellers" in t:
                temp = temp.find_next('a')
                t = temp["href"]
            link = "https://www.amazon.in" + t
            print(link)
        except:
            link = "N/A"
        
        try:
            title = i.find('img', attrs = {"class":"s-image"})["alt"]
        except:
            title = "N/A"
        
        try:
            img = i.find('img', attrs = {"class":"s-image"})["src"]
        except:
            img = "N/A"

        stars = i.find('div', attrs = {"class": "a-size-small"})
        if stars:
            stars = stars.find('span')["aria-label"]
        else:
            stars = "N/A"

        try:
            price = i.find('span', attrs = {"class": "a-price"}).find("span").text
        except:
            price = "N/A"
        
        data.append(Data(link,title,img,price.lstrip("₹"),stars))
    return data




if __name__ == '__main__':
    k = input()
    elems = get_links(k)
    for i in elems:
        print(i)
