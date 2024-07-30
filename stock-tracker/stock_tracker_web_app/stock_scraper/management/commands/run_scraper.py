from django.core.management.base import BaseCommand
from stock_scraper.scrape_data import get_stock_data, TICKERS

class Command(BaseCommand):
    help = 'Scrape stock data and save it to the database'

    def handle(self, *args, **options):
        for ticker in TICKERS:
            get_stock_data(ticker)
