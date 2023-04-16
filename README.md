# SwiftScore - Kotlin Sucks

## Introduction

SwiftScore is a project designed to help customers make informed decisions by analyzing the sentiment of product reviews. With this, customers can quickly and easily check out the sentiment of reviews on different aspects of a product, such as its quality, price, durability, and customer service.

It collects reviews from e-commerce websites (Amazon, eBay) and applies sentiment analysis on the reviews. The sentiment analysis algorithm can identify whether a review is positive, negative, or neutral regarding a certain keyword.

In summary, SwiftScore is a valuable tool for customers looking to quickly and easily check the reviews' sentiment regarding specific aspects of a product.

## How it was built

Elements were scraped from amazon.in and ebay.com(can be expanded) using a combination of `selenium` and `bs4`. Selenium was used to scrape elements loaded in through js or to access links through a webpage. `textblob` was used to analyse the positivity or negativity of sentences in reviews containing the keywords. The front end is made using a combination of `flask` and `html`. The scraped and processed data is displayed on a website that's hosted locally but can be hosted online easily as well.


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

These instructions assume that Python version 3.8 or higher has been installed on the system and is on the `PATH` in case of Windows. A matching chromedriver also needs to be installed and added to path. The driver can be downloaded from [here](https://chromedriver.chromium.org/downloads).

1. Install dependencies: Make sure you're in the same directory as `requirements.txt` and enter the following on the command line:  
    a. macOS/Linux:  `python3 -m pip install -r requirements.txt`  
    b. Windows: `pip install -r requirements.txt`

2. Run the flask server: Make sure you're in the same directory as `app.py` and enter `flask run` on the command line.

3. A hyperlink to the server will show up on the command line. Follow that link to reach the local host. You can access the site using this link.

## Steps to use this project

1. Head over to the search bar on the home page, and type in the name of the product you want to see.

2. A list of items comes up from various e-commerce sites. Click on the name of the one you want to visit.

3. Enter the keyword you want to search the sentiment for.

4. A value shows up that is classified to be neutral/positive/negative. A 0 value stands for a neutral outlook of the reviews on the topic. The more positive the value the better the reviews about that certain part of the product, and vice versa for negative values.

## Team members
Team name: Kotlin Sucks

1. Ayush Gupta IMT2022546

2. Harsh Modani IMT2022055