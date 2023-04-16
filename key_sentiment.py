import requests
from bs4 import BeautifulSoup
from get_comments import get_keywords
from textblob import TextBlob

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
                for sent in comment_text.split('.'):
                    sent = sent.strip()
                    if i in sent:
                        sent_blob = TextBlob(sent)
                        comment_score+=sent_blob.sentiment.polarity
                        sent_num+=1
                
                if comment_score!=0:
                    comment_num+=1
                    comment_score /=sent_num
                key_score+=comment_score
            
            if key_score!=0:
                key_score/= comment_num
            d[i] = key_score
        print(d)
        return d
    
    if 'https://www.ebay.com' in url:
        



link = "https://www.amazon.in/roboCraze-Arduino-Development-Board-cable/dp/B07G4C4D8F"
keys = get_keywords(link)
get_sent(link,keys)