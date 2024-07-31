from celery import shared_task
from .scrape_data import get_stock_data, TICKERS

@shared_task
def scrape_stock_data():
    for ticker in TICKERS:
        get_stock_data(ticker)