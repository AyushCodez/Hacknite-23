# importing libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
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

    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions() 
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver.get(URL)
    time.sleep(1)
    element = driver.find_element(By.CLASS_NAME,"cr-widget-TitleRatingsHistogram")

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    r = driver.page_source

    soup = BeautifulSoup(r, "html.parser")
	
    para = soup.find_all('span', attrs = {"data-action":"reviews:filter-action:apply"})
    ret = []
    for i in para:
        ret.append(i.text.strip())
        print(ret[-1])

    driver.quit()
    return ret

def get_links(keyword: str):
    
    keyword = keyword.replace(" ", "+")
    HEADERS = ({'User-Agent':'Chrome/44.0.2403.159', 'Accept-Language': 'en-US, en;q=0.5'})

    #web scraping amazon search results and getting details of each link

    r = requests.get(f"https://www.amazon.in/s?k={keyword}", headers=HEADERS)

    soup = BeautifulSoup(r.content,"html.parser")

    elem = soup.find_all('div', attrs= {"data-component-type":"s-search-result"})

    data = []
    for i in elem:
        flag = False
        try:
            temp = i.find('a')
            t = temp["href"]
            while "bestsellers" in t:
                temp = temp.find_next('a')
                t = temp["href"]
            link = "https://www.amazon.in" + t
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
            flag = True
        else:
            stars = "N/A"

        try:
            price = i.find('span', attrs = {"class": "a-price"}).find("span").text
        except:
            price = "N/A"
        
        if flag:
            data.append(Data(link,title,img,price,stars))

    
    #web scraping ebay search results and getting details of each link
    r = requests.get(f"https://www.ebay.com/sch/i.html?&_nkw={keyword}", headers= HEADERS)
    soup = BeautifulSoup(r.content,"html.parser")

    elem = soup.find_all('li', attrs= {"class":"s-item"})
    if elem:
        elem = elem[1:]

    for i in elem:
        image = i.find('div', attrs = {"class": "s-item__image-wrapper"})
        if(img):
            img = image.find('img')['src']
            title = image.find('img')['alt']
        else:
            img = title = "N/A"
        
        link = i.find('div', attrs = {"class": "s-item__image"})
        if(link):
            link = link.find('a')['href']
            link = link[:link.find('?')]
        else:
            link = "N/A"

        price = i.find('span', attrs = {"class":"s-item__price"})
        if(price):
            price = price.text
        else:
            price = "N/A"

        stars = i.find('div', attrs = {"class": "x-star-rating"})
        flag = False
        if(stars):
            stars = stars.find('span').text
            flag = True
        else:
            stars = "N/A"
        

        # print("Title: ", title)
        # print("Image: ", img)
        # print("Link: ", link)
        # print("Price: ", price)
        # print("Stars: ",stars)
        if flag:
            data.append(Data(link,title,img,price,stars))
    return data




if __name__ == '__main__':
    k = input()
    elems = get_links(k)
    for i in elems:
        print(i)
