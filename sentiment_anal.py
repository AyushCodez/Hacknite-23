from textblob import TextBlob

# Define a function to get the sentiment of a given text
def get_sentiment(text):
    text = TextBlob(text).correct()
    sentiment = text.sentiment.polarity
    return sentiment

# Use the model to predict the sentiment of a new text
text = "Winning the lottery was the most incredible moment of my life, it felt like all my dreams had come true."
sentiment = get_sentiment(text)
print(sentiment) # Output: 'positive'
