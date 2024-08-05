from celery import shared_task
from django.core.mail import send_mail, get_connection
from .models import Stock, Subscriber
from .scrape_data import get_stock_data, save_data_to_csv
from .config import TICKERS

@shared_task
def scrape_stock_data():
    stock_data = []
    for ticker in TICKERS:
        stock_data.append(get_stock_data(ticker))
    
    # Save data to CSV (if needed)
    save_data_to_csv(stock_data)
    
    # Send email updates to subscribers
    send_email_updates(stock_data)

def send_email_updates(stock_data):
    connection = get_connection()
    
    try:
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            message = "Stock Price Updates:\n\n"
            for stock in stock_data:
                message += f"{stock['ticker']}: {stock['current_price']}\n"
            
            send_mail(
                'Stock Updates',
                message,
                'i2istockupdates@yahoo.com',
                [subscriber.email],
                connection=connection,
            )
    finally:
        connection.close()