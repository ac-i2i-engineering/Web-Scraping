from celery import shared_task
from django.core.mail import send_mail
from .models import Stock, Subscriber
from .scrape_data import get_stock_data, save_data_to_csv
from .config import TICKERS

@shared_task
def scrape_stock_data():
    stock_data = []
    for ticker in TICKERS:
        stock_data.append(get_stock_data(ticker))

    save_data_to_csv(stock_data)

    # Fetch updated stock data for email
    updated_stocks = Stock.objects.all()
    stock_info = "\n".join([f"{stock.ticker_symbol}: {stock.current_price} ({stock.change}%)" for stock in updated_stocks])

    # Send email to all subscribers
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        send_mail(
            'Stock Price Update',
            f'Here are the latest stock prices:\n\n{stock_info}',
            'i2istocktracker@gmail.com',
            [subscriber.email],
            fail_silently=False,
        )