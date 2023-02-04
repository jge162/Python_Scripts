import requests

url = "https://data.cnn.com/breaking_news/domestic.json"
response = requests.get(url)

data = response.json()

for article in data:
    print(article)

# specify the URL of the breaking news API
url = 'https://data.cnn.com/breaking_news/domestic.json'

# make an HTTP GET request to the API
response = requests.get(url)

# check the status code of the response to make sure the request was successful
if response.status_code == 200:
    # the request was successful, parse the JSON data
    data = response.json()

    print(data)  # debug: print the contents of data

    # extract the headline and summary of each article
    for article in data['articles']:
        headline = article['headline']
        summary = article['summary']

        # print the headline and summary
        print('Headline:', headline)
        print('Summary:', summary)
        print('---')
else:
    # the request was not successful, print an error message
    print(f'Failed to retrieve breaking news, status code: {response.status_code}')

"""
sudo python3 /Users/home/Documents/GitHub/Python_Scripts/Scrap_Latestnews.py
"""
