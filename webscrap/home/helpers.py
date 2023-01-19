from bs4 import BeautifulSoup#create and beautify our html content
import requests#access data from other website
from .models import *
def get_all_stocks_urls():
    try:
        page = requests.get('https://stocks.zerodha.com/')
        soup = BeautifulSoup(page.content, features='html.parser')
        # print(soup)#isse list ajayegi stocks ki
        #page.content--will get all the html codes
        for ul in soup.find_all('div', class_="index-page"):
            for li in ul.findAll('li'):
                anchor_tag = li.find('a')
                print(anchor_tag['href'])
                print()
                Stocks.objects.get_or_create(
                    stock_name = anchor_tag.text,
                    stock_url = anchor_tag['href']

                )#this is for displaying of data in db.

    except Exception as e:
        print(e)