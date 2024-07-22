import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_stock_data(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {}
    data['ticker'] = ticker
    data['price'] = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
    data['change'] = soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text
    data['volume'] = soup.find('td', {'data-test': 'TD_VOLUME-value'}).find('span').text

    return data

tickers = ['AAPL', 'GOOGL', 'MSFT']
stock_data = []

for ticker in tickers:
    stock_data.append(get_stock_data(ticker))

df = pd.DataFrame(stock_data)
print(df)

df.to_csv('stock_data.csv', index=False)
