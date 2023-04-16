import requests
from bs4 import BeautifulSoup
from get_comments import get_keywords
from textblob import TextBlob
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def get_sent(url: str, keys: list)->float:
    
    HEADERS = ({'User-Agent':'Chrome/44.0.2403.159', 'Accept-Language': 'en-US, en;q=0.5'})
    d = dict()

    if 'https://www.amazon.in' in url:
        url = url.replace("/dp/","/product-reviews/") + "/"
        for i in keys:
            temp = url + "/?filterByKeyword=" + i.replace(" ","+")
            response = requests.get(temp, headers=HEADERS)
            soup = BeautifulSoup(response.text, 'html.parser')
            comment_elements = soup.find_all('div', {'data-hook': 'review'})
            key_score = 0
            comment_num = 0
            for comment_element in comment_elements:
                
                comment_score = 0
                sent_num = 0
                comment_text = comment_element.find('span', {'data-hook': 'review-body'}).text
                flag = False
                for sent in comment_text.split('.'):
                    
                    sent = sent.strip()
                    sent = sent.lower()
                    if i.lower() in sent:
                        flag = True
                        sent_blob = TextBlob(sent)
                        comment_score+=sent_blob.sentiment.polarity
                        sent_num+=1
                
                if flag:
                    comment_num+=1
                    if sent_num!=0:
                        comment_score /=sent_num
                key_score+=comment_score
            
            if key_score!=0:
                key_score/= comment_num
            

            if comment_num >=3:
                d[i] = key_score
        print(d)
        return d
    
    if 'https://www.ebay.com' in url:
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions() 
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver.get(url)

        div1 = driver.find_element(By.CLASS_NAME, "reviews-right")
        div = div1.find_element(By.CLASS_NAME, "reviews-header")

        
        time.sleep(1)

        button = div.find_element(By.CLASS_NAME, "sar-btn")
        button.click()
        new_url = driver.current_url
        driver.close()

        for i in keys:
            temp = new_url + "&q=" + i.replace(" ","+")
            response = requests.get(temp, headers=HEADERS)
            soup = BeautifulSoup(response.text, 'html.parser')
            comment_elements = soup.find_all('div', {'class':'ebay-review-section'})
            key_score = 0
            comment_num = 0
            for comment_element in comment_elements:
                comment_score = 0
                sent_num = 0
                flag = False
                comment_text = comment_element.find('p', {'itemprop':'reviewBody'}).text
                for sent in comment_text.split('.'):
                    sent = sent.strip()
                    sent = sent.lower()
                    if i.lower() in sent:
                        flag = True
                        sent_blob = TextBlob(sent)
                        comment_score+=sent_blob.sentiment.polarity
                        sent_num+=1
                
                if flag:
                    comment_num+=1
                    if sent_num!=0:
                        comment_score /=sent_num
                key_score+=comment_score
            
            if key_score!=0:
                key_score/= comment_num
            
            if comment_num >=3:
                d[i] = key_score
            else:
                d[i] = 0
        print(d)
        return d
        
        
if __name__ == '__main__':
    link = "https://www.amazon.in/HP-Gaming-Mouse-G200-7QV30AA/dp/B08498186T"
    link = "https://www.ebay.com/itm/185829460367"
    link = "https://www.amazon.in/Redgear-Gaming-Semi-Honeycomb-Design-Windows/dp/B09GP6CHJZ"
    keys = get_keywords(link)
    #keys = ["value for money"]  
    get_sent(link,keys)