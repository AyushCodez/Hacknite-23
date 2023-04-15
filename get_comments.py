# importing libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def get_keywords(URL):

    driver.get(URL)
    time.sleep(1)
    element = driver.find_element(By.CLASS_NAME,"cr-widget-TitleRatingsHistogram")

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    a = driver.find_elements(By.CLASS_NAME,"a-declarative")
    
    # ans = 0
    
    # for i in a:
    #     if i.get_attribute("data-action") == "reviews:filter-action:apply":
    #         ans+=1
    #         print(i.text)
    
    # print(ans, "LOOK HERE")

    r = driver.page_source


    soup = BeautifulSoup(r, "html.parser")

    with open("temp.html","w",encoding="utf-8") as f:
        f.write(str(soup))
	
    para = soup.find_all('span', attrs = {"data-action":"reviews:filter-action:apply"})
    
    for i in para:
        print(i.text.strip())
def get_links(keyword):

    HEADERS = ({'User-Agent':'Chrome/44.0.2403.157', 'Accept-Language': 'en-US, en;q=0.5'})
    r = requests.get(f"https://www.amazon.in/s?k={keyword}", headers= HEADERS)

    soup = BeautifulSoup(r.content,"html.parser")

    with open("temp.html","w",encoding="utf-8") as f:
        f.write(str(soup))
	

    elem = soup.find_all('div', attrs= {"data-component-type":"s-search-result"})

    links = []
    for i in elem:
        temp = i.find('a')
        t = temp["href"]
        while "bestsellers" in t:
            temp = temp.find_next('a')
            t = temp["href"]
        links.append("https://www.amazon.in" + t)
    return links




if __name__ == '__main__':
    k = input()
    links = get_links(k)
    #links = ["https://www.amazon.in/Xbox-Series-S/dp/B08J89D6BW"]
    for link in links:
        print(link)
        get_keywords(link)
