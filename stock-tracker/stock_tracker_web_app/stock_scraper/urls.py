from django.urls import path
from . import views

'''
Add your views to urls here
'''

urlpatterns = [
    path('', views.index, name='index'),
]   