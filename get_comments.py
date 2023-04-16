# importing libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Data:

    def __init__(self, link: str, name: str, image: str, price: str, rating: str):
        self.link, self.name, self.image, self.price, self.rating = link, name, image, price, rating
        if (len(self.name) >= 40): #shortening name to fit in screen
            self.name = self.name[0:38]+'...'
    
    def __repr__(self) -> str:
        string = f"""Link: {self.link}
        Name: {self.name}
        Image: {self.image}
        Price: {self.price}
        Rating: {self.rating}"""

        return string

def get_keywords(URL):

    if 'https://www.amazon.in' in URL:

        options = webdriver.ChromeOptions() 
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless')
        options.headless = True
        driver = webdriver.Chrome(options=options)

        driver.get(URL)
        time.sleep(3) #waiting for the keywords to load in the page
        element = driver.find_element(By.CLASS_NAME,"cr-widget-TitleRatingsHistogram")

        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

        r = driver.page_source

        soup = BeautifulSoup(r, "html.parser")
        
        para = soup.find_all('span', attrs = {"data-action":"reviews:filter-action:apply"})

        ret = []
        for i in para:
            if(i.text.strip()):
                ret.append(i.text.strip()) #getting all the keywords of a specific url
                print(ret[-1])

        driver.quit()

        return ret
    
    return [] #ebay links do not have keywords.

def get_links(keyword: str):
    
    keyword = keyword.replace(" ", "+")
    HEADERS = ({'User-Agent':'Chrome/44.0.2403.159', 'Accept-Language': 'en-US, en;q=0.5'})

    #web scraping amazon search results and getting details of each link

    r = requests.get(f"https://www.amazon.in/s?k={keyword}", headers=HEADERS) #getting the search results from amazon

    soup = BeautifulSoup(r.content,"html.parser")

    elem = soup.find_all('div', attrs= {"data-component-type":"s-search-result"})

    data = []
    for i in elem:
        flag = False

        try: #getting link to search result
            temp = i.find('a')
            t = temp["href"]

            while "bestsellers" in t: #in case of result being besteller on amazon, handling case.
                temp = temp.find_next('a')
                t = temp["href"]

            link = "https://www.amazon.in" + t
        except:
            link = "N/A"
        
        try:
            title = i.find('img', attrs = {"class":"s-image"})["alt"] #getting title and link to thumbnail of image
            img = i.find('img', attrs = {"class":"s-image"})["src"]
        except:
            img = "N/A"
            title = "N/A"

        stars = i.find('div', attrs = {"class": "a-size-small"})
        if stars:
            stars = stars.find('span')["aria-label"] #finding rating of search result
            flag = True
        else:
            stars = "N/A"

        try:
            price = i.find('span', attrs = {"class": "a-price"}).find("span").text #getting price
        except:
            price = "N/A"
        
        if flag:
            data.append(Data(link,title,img,price,stars)) #only adding to list if search result has rating

    
    #web scraping ebay search results and getting details of each link
    r = requests.get(f"https://www.ebay.com/sch/i.html?&_nkw={keyword}", headers= HEADERS) #getting ebay search results
    soup = BeautifulSoup(r.content,"html.parser")

    elem = soup.find_all('li', attrs= {"class":"s-item"})
    if elem: #removing heading element
        elem = elem[1:]

    for i in elem:
        image = i.find('div', attrs = {"class": "s-item__image-wrapper"})
        if(img): #getting image and title
            img = image.find('img')['src']
            title = image.find('img')['alt']
        else:
            img = title = "N/A"
        
        link = i.find('div', attrs = {"class": "s-item__image"})
        if(link): #getting link to search result
            link = link.find('a')['href']
            link = link[:link.find('?')]
        else:
            link = "N/A"

        price = i.find('span', attrs = {"class":"s-item__price"})
        if(price): #getting price
            price = price.text
        else:
            price = "N/A"

        stars = i.find('div', attrs = {"class": "x-star-rating"})
        flag = False
        if(stars): #getting rating
            stars = stars.find('span').text
            flag = True
        else:
            stars = "N/A"
        
        if flag:
            data.append(Data(link,title,img,price,stars)) #only adding to list if search result has rating
    return data #returning list of Data objects




if __name__ == '__main__': #test code
    k = input()
    elems = get_links(k)
    for i in elems:
        print(i)
