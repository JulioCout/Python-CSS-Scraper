from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def scrape(request):
    page = requests.get('http://google.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    
    link_address = []

    for link in soup.find_all('a'):
        link_address.append(link.get('href'))

    return render(request, 'myapp/result.html', {'link_address': link_address})