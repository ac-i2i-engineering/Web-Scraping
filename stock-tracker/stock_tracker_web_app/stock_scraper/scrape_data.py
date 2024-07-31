import requests
from bs4 import BeautifulSoup
import pandas as pd
from .config import TICKERS, CSV_FILENAME
from decimal import Decimal

def get_stock_data(ticker):
    from .models import Stock
    
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {}
    data['ticker'] = ticker
    
    # Handle possible None types gracefully
    price_element = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
    change_element = soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'})
    volume_element = soup.find('td', {'data-test': 'TD_VOLUME-value'})
    
    if price_element:
        price_text = price_element.text.replace(',', '')
        data['price'] = Decimal(price_text)
    else:
        data['price'] = None
    
    if change_element:
        data['change'] = change_element.text
    else:
        data['change'] = None
    
    if volume_element:
        volume_span = volume_element.find('span')
        if volume_span:
            volume_text = volume_span.text.replace(',', '')
            data['volume'] = int(volume_text)
        else:
            data['volume'] = None
    else:
        data['volume'] = None
    
    # Save data to Django model
    stock, created = Stock.objects.get_or_create(ticker_symbol=data['ticker'])
    stock.current_price = data['price']
    stock.volume = data['volume']
    stock.save()

    return data

def save_data_to_csv(stock_data, filename=CSV_FILENAME):
    df = pd.DataFrame(stock_data)
    df.to_csv(filename, index=False)

if __name__ == '__main__':
    stock_data = []

    for ticker in TICKERS:
        stock_data.append(get_stock_data(ticker))

    save_data_to_csv(stock_data)