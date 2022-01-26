from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver as wd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

import time

# Create your views here.

def food(request):
    return render(request, 'infoplus/food.html')    

def insta(request):
    return render(request, 'infoplus/insta.html')

# map click
def button(request):
    return render(request, 'infoplus/button.html')