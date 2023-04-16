import requests
from bs4 import BeautifulSoup
from get_comments import get_keywords
from textblob import TextBlob
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def get_sent(url: str, keys: list)->dict: #gets dictionary of each keyword correspinding to sentiment of reviews

    print(keys)
    
    HEADERS = ({'User-Agent':'Chrome/44.0.2403.159', 'Accept-Language': 'en-US, en;q=0.5'}) #to pass through bot checkers
    d = dict()

    if 'https://www.amazon.in' in url: #if link is of amazon
        url = url.replace("/dp/","/product-reviews/") + "/" #getting the comments page
        for key in keys:
            if(key is not None):
                temp = url + "/?filterByKeyword=" + key.replace(" ","+") #getting comments containing keyword and scraping them
                response = requests.get(temp, headers=HEADERS)
                soup = BeautifulSoup(response.text, 'html.parser')
                comment_elements = soup.find_all('div', {'data-hook': 'review'}) #getting all individual reviews
                key_score = 0
                comment_num = 0
                for comment_element in comment_elements:
                    
                    comment_score = 0
                    sent_num = 0
                    comment_text = comment_element.find('span', {'data-hook': 'review-body'}).text #finding the review content
                    flag = False
                    for sent in comment_text.split('.'):
                        
                        sent = sent.strip()
                        sent = sent.lower()
                        if key.lower() in sent: #checking if keyword in review
                            flag = True
                            sent_blob = TextBlob(sent)
                            comment_score+=sent_blob.sentiment.polarity #calculating the sentiment and finding a average
                            sent_num+=1
                    
                    if flag:
                        comment_num+=1
                        if sent_num!=0:
                            comment_score /=sent_num
                    key_score+=comment_score    #calculating the score
                
                if key_score!=0:
                    key_score/= comment_num
                

                if comment_num >=3:
                    d[key] = round(key_score,4) #setting the appropriate key value pair
                else:
                    d[key] = 0
    
    if 'https://www.ebay.com' in url: #if link is of ebay.com
        options = webdriver.ChromeOptions() 
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless')
        options.headless = True
        driver = webdriver.Chrome(options=options)

        driver.get(url) #selenium to get the page with all comments

        div1 = driver.find_element(By.CLASS_NAME, "reviews-right")
        div = div1.find_element(By.CLASS_NAME, "reviews-header")

        
        time.sleep(1)

        button = div.find_element(By.CLASS_NAME, "sar-btn")
        button.click()
        new_url = driver.current_url #stroing the url of the comments page
        driver.close()

        for key in keys: #similar code as in case of amazon.in
            temp = new_url + "&q=" + key.replace(" ","+")
            response = requests.get(temp, headers=HEADERS)
            soup = BeautifulSoup(response.text, 'html.parser')
            comment_elements = soup.find_all('div', {'class':'ebay-review-section'})
            key_score = 0
            comment_num = 0
            for comment_element in comment_elements:
                comment_score = 0
                sent_num = 0
                flag = False
                comment_text = comment_element.find('p', {'itemprop':'reviewBody'})
                if(comment_text):
                    comment_text = comment_text.text
                    for sent in comment_text.split('.'):
                        sent = sent.strip()
                        sent = sent.lower()
                        if key.lower() in sent:
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
                d[key] = round(key_score,4)
            else:
                d[key] = 0
    print(d)
    return d #returning dictionary
        
        
if __name__ == '__main__': #test code
    link = "https://www.amazon.in/HP-Gaming-Mouse-G200-7QV30AA/dp/B08498186T"
    link = "https://www.ebay.com/itm/185829460367"
    link = "https://www.amazon.in/Redgear-Gaming-Semi-Honeycomb-Design-Windows/dp/B09GP6CHJZ"
    keys = get_keywords(link)
    #keys = ["value for money"]  
    get_sent(link,keys)