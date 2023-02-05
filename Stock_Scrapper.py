import pandas as pd
import requests


def get_stock_tickers():
    table = pd.read_html(
        'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
    tickers = table['Symbol'].tolist()
    tickers.sort()
    my_stocks = ['AAPL', 'TSLA', 'WFC', 'KO', 'BAC']
    #  print(tickers[:10])
    return [ticker for ticker in my_stocks if ticker in tickers]


def get_stock_prices(ticker_list):
    API_KEY = 'API_KEY_HERE'
    for ticker in ticker_list:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        print(f"{ticker} is {data['Global Quote']['05. price']}")


def main():
    all_tickers = get_stock_tickers()
    get_stock_prices(all_tickers)


if __name__ == '__main__':
    main()

"""
pip install pandas
pip install lxml
sudo python3 /Users/home/Documents/GitHub/Python_Scripts/Stock_Scrapper.py
Go to this website to get free API key https://www.alphavantage.co/support/#api-key
"""
