from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock, Subscriber

def index(request):
    stocks = Stock.objects.all()
    context = {
        'stocks': stocks,
    }
    return render(request, 'stock_scraper/index.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.error(request, 'Email already subscribed!')
            else:
                Subscriber.objects.create(email=email)
                messages.success(request, 'Subscribed successfully!')
    return redirect('index')
