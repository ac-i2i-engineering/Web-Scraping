from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock

def index(request):
    stocks = Stock.objects.all()
    context = {
        'stocks': stocks,
    }
    return render(request, 'stock_scraper/index.html', context)