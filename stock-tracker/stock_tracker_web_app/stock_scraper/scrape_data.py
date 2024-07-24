import requests
from bs4 import BeautifulSoup
import pandas as pd
from config import TICKERS, CSV_FILENAME

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

def save_data_to_csv(stock_data, filename=CSV_FILENAME):
    df = pd.DataFrame(stock_data)
    df.to_csv(filename, index=False)

if __name__ == '__main__':
    stock_data = []

    for ticker in TICKERS:
        stock_data.append(get_stock_data(ticker))

    save_data_to_csv(stock_data)
