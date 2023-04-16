# SwiftScore - Kotlin Sucks

## Introduction

SwiftScore is a project designed to help customers make informed decisions by analyzing the sentiment of product reviews. With this, customers can quickly and easily check out the sentiment of reviews on different aspects of a product, such as its quality, price, durability, and customer service.

It collects reviews from e-commerce websites (Amazon and eBay) and applies sentiment analysis on the reviews. The sentiment analysis algorithm can identify whether a review is positive, negative, or neutral and can also identify the specific aspects of the product.

In summary, SwiftScore is a valuable tool for customers looking to quickly and easily check the sentiment of product reviews and make informed purchasing decisions.

## Steps to use this project

1. Head over to the search bar on the home page, and type in the name of the product you want to see.

2. A list of items comes up. Click on the name of the one you want to visit.

3. Enter the keyword you want to search the sentiment for.

## Dependencies
 This project uses the following dependencies:

```
beautifulsoup4
requests
selenium
flask
textblob 
```

## How to run the project

1. Install dependencies: Make sure you're in the same directory as `requirements.txt` and enter the following on the command line:  
    a. macOS/Linux:  `python3 -m pip install -r requirements.txt`  
    b. Windows: `pip install -r requirements.txt`

2. Run the flask server: Make sure you're in the same directory as `app.py` and enter `flask run` on the command line.

3. A hyperlink to the server



