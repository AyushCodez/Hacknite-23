import requests
from bs4 import BeautifulSoup
from get_comments import get_keywords
from textblob import TextBlob

def get_sentiment(url: str, targets: list)->float:

    HEADERS = ({'User-Agent':'Chrome/44.0.2403.159', 'Accept-Language': 'en-US, en;q=0.5'})
    response = requests.get(url, headers=HEADERS)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the section of the HTML that contains the comments and reviews
    comments_section = soup.find('div', {'id':"cm-cr-dp-review-list"})

    # Find all the comment elements within the comments section
    comment_elements = comments_section.find_all('div', {'data-hook': 'review'})

    # Initialize a variable to store the overall sentiment score
    overall_sentiment_score = 0.0

    # Loop through each comment element and check if it contains the target keyword
    for target_keyword in targets:
        print(target_keyword)
        com_num = 0
        for comment_element in comment_elements:
            comment_text = comment_element.find('span', {'data-hook': 'review-body'}).text
            
            # Split the comment text into sentences
            sentences = comment_text.split('.')
            
            # Initialize a variable to store the sentiment scores of the sentences
            sentence_sentiment_scores = []
            
            # Loop through each sentence and check if it contains the target keyword
            for sentence in sentences:
                if target_keyword in sentence.lower():
                    # Use TextBlob to get the sentiment score of the sentence
                    sentence_blob = TextBlob(sentence)
                    sentence_sentiment_scores.append(sentence_blob.sentiment.polarity)
            
            # Calculate the sentiment score of the comment by averaging the sentiment scores of the
            # sentences that contain the target keyword
            if sentence_sentiment_scores:
                com_num+=1
                comment_sentiment_score = sum(sentence_sentiment_scores) / len(sentence_sentiment_scores)
            else:
                comment_sentiment_score = 0.0
            
            # Add the sentiment score of the comment to the overall sentiment score
            overall_sentiment_score += comment_sentiment_score
            
            # Print the comment and its sentiment score for debugging purposes
            print(comment_text)
            print('Sentiment Score:', comment_sentiment_score)
            print()
        
        # Calculate the overall sentiment score by dividing the sum of the comment sentiment scores
        # by the total number of comments
        
        if com_num!=0:
            overall_sentiment_score /= com_num
        

        # Print the overall sentiment score
        print(target_keyword, ' :Overall Sentiment Score:', overall_sentiment_score)

a = get_keywords("https://www.amazon.in/HP-Gaming-Mouse-G200-7QV30AA/dp/B08498186T?th=1")
get_sentiment("https://www.amazon.in/HP-Gaming-Mouse-G200-7QV30AA/dp/B08498186T?th=1",a)