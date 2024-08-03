from celery import shared_task
from django.core.mail import send_mail
from .models import Stock
from .scrape_data import get_stock_data, save_data_to_csv
from .config import TICKERS

@shared_task
def scrape_stock_data():
    stock_data = []
    for ticker in TICKERS:
        stock_data.append(get_stock_data(ticker))