import requests
from bs4 import BeautifulSoup

# specify the URL of the website containing the news
url = 'https://www.example.com/news'

# make an HTTP GET request to the website
response = requests.get(url)

# parse the HTML content of the response
soup = BeautifulSoup(response.text, 'html.parser')

# find all the news articles on the page
articles = soup.find_all('article')

# extract the headline and summary of each article
for article in articles:
    headline = article.find('h2').text
    summary = article.find('p').text
    
    # print the headline and summary
    print('Headline:', headline)
    print('Summary:', summary)
    print('---')
