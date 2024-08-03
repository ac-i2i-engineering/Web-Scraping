import requests
from bs4 import BeautifulSoup
import pandas as pd
from decimal import Decimal, InvalidOperation
from .config import TICKERS, CSV_FILENAME

def get_stock_data(ticker):
    from .models import Stock  # Move import here
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {}
    data['ticker'] = ticker
    
    # Extract elements for price, previous close, open, day's range, and volume
    price_element = soup.find('fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketPrice'})
    previous_close_element = soup.find('fin-streamer', {'data-field': 'regularMarketPreviousClose'})
    open_element = soup.find('fin-streamer', {'data-field': 'regularMarketOpen'})
    day_range_element = soup.find('fin-streamer', {'data-field': 'regularMarketDayRange'})
    volume_element = soup.find('fin-streamer', {'data-field': 'regularMarketVolume'})

    if price_element:
        price_text = price_element.text.replace(',', '')
        try:
            data['current_price'] = Decimal(price_text)
        except InvalidOperation:
            data['current_price'] = None
    else:
        data['current_price'] = None

    if previous_close_element:
        previous_close_text = previous_close_element.text.replace(',', '')
        try:
            data['previous_close_price'] = Decimal(previous_close_text)
        except InvalidOperation:
            data['previous_close_price'] = None
    else:
        data['previous_close_price'] = None

    if open_element:
        open_text = open_element.text.replace(',', '')
        try:
            data['open_price'] = Decimal(open_text)
        except InvalidOperation:
            data['open_price'] = None
    else:
        data['open_price'] = None

    if day_range_element:
        day_range_text = day_range_element.text.replace(',', '')
        try:
            range_parts = day_range_text.split(' - ')
            data['low_price'] = Decimal(range_parts[0].replace(',', ''))
            data['high_price'] = Decimal(range_parts[1].replace(',', ''))
        except (InvalidOperation, IndexError):
            data['low_price'] = None
            data['high_price'] = None
    else:
        data['low_price'] = None
        data['high_price'] = None

    if volume_element:
        volume_text = volume_element.text.replace(',', '')
        try:
            data['volume'] = int(volume_text)
        except ValueError:
            data['volume'] = None
    else:
        data['volume'] = None

    print(ticker)
    print(f"Current Price: {data['current_price']}")
    print(f"Previous Close: {data['previous_close_price']}")
    print(f"Open: {data['open_price']}")
    print(f"Day's Range: {data['low_price']} - {data['high_price']}")
    print(f"Volume: {data['volume']}")

    # Save data to Django model
    stock, created = Stock.objects.get_or_create(ticker_symbol=data['ticker'])
    stock.current_price = data['current_price']
    stock.previous_close_price = data['previous_close_price']
    stock.open_price = data['open_price']
    stock.high_price = data['high_price']
    stock.low_price = data['low_price']
    stock.volume = data['volume']
    # Assuming `market_cap`, `pe_ratio`, and `change` are not included in this request
    # stock.market_cap = data.get('market_cap', None)
    # stock.pe_ratio = data.get('pe_ratio', None)
    # stock.change = data.get('change', None)
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