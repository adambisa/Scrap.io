import requests
from bs4 import BeautifulSoup
import re
from uuid import uuid1
# from flask import Flask,request


'''
app = Flask(__name__)
app.get('/')
def home():
    return 'welcome to my web'
app.post('/')
def recieve():
    id = request.args.get('id')
    url = request.args.get('url')
    price = request.args.get('price')
    emails = request.args.get('email')
    timestamp = request.args.get('timestamp')
    
    

'''


class Scraper():
    def __init__(self) -> None:
        self.price_pattern = re.compile(
            r'([0-9]+?\s?[,.][0-9]+)|([0-9]?\s[0-9]+?,[0-9]+)|(>[0-9]?\s[0-9]+?,[0-9]+)')
        self.name_pattern = re.compile(r'(([A-Z]{1}[a-zA-Z]+)\s)+')  # TODO
    def clean_up_price(self, price: str) -> str:
        price = re.sub(r'[^\d.,]', '', price)
        return price

    def validate_url(self, url: str) -> bool:
        valid_url = re.compile(r'^https:\/\/www.[a-zA-Z]+.sk\/[a-z-.0-9\/]+$')
        if valid_url.match(url):
            return True
        else:
            return False

    def scrape_any(self, url: str) -> str:

        if not self.validate_url(url):
            return None
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'lxml')

        if soup.find(class_='price-box__price') is not None:
            cont = soup.find(class_='price-box__price')
            price = self.price_pattern.match(cont.text).group()
        elif soup.find(class_='price-wrap') is not None:
            cont = soup.find(class_='price-wrap')
            cont = str(cont)
            price = [i for i in cont if i.isnumeric() == True or i ==
                     ',' or i == '.']
            price = ''.join(price)
            return price
        elif soup.find(class_='product__discount-price product__discount-price--no-border d-lg-flex justify-content-between align-items-center mb-1 mb-lg-0 text-center text-lg-left typo-complex-14') is not None:
            cont = soup.find(
                class_='d-block ml-lg-3 typo-complex-22 typo-complex-lg-32 text-nowrap')
            price = self.price_pattern.match(cont.text).group()
        else:
            return 'zly link'
        price = self.clean_up_price(price)
        return price

    # implement url parameter base_url,
    def scrape_cheapest_datart(self, product: str) -> dict:
        results = dict()
        default_url = 'https://www.datart.sk'
        query = f'/vyhladavanie?q={product}'
        page = requests.get(default_url+query)
        soup = BeautifulSoup(page.content, 'lxml')

        #recreate struct {name:(url,price)}
        listik = list()
        for link in soup.find_all(class_='page-link'):
            listik.append(link.text.encode('utf-8'))
        listik = listik[1:-1]
        last_page = int(listik[-1])
        for page_index in range(1, last_page+1): 
            search = requests.get(f'https://www.datart.sk/vyhladavanie?q={product}&page={page_index}')
            body = BeautifulSoup(search.content, 'lxml')
            names = body.find_all('h3', {'class' : 'item-title'})
            prices = body.find_all(class_ = 'actual')
            product_links = list()
            for a in names:
                product_links.append(a.a.get('href'))

            for name in names:
                n = name.text
                for price in prices:
                    for link in product_links:
                        p = price.text
                        p = self.clean_up_price(p)
                        results[n] = (default_url+link,p)
        cheapest = min(results, key=results.get)
        return cheapest, results[cheapest]
# testy     


'''
print(scrape_any('https://www.alza.sk/hobby/konferencny-stolik-montana-130-70-cm-vyska-45-cm-podnozie-a-d7144761.htm'), 'alza')
print(scrape_any('https://www.nay.sk/apple-macbook-pro-16-m1-pro-512gb-2021-mk183sl-a-vesmirne-sivy'), 'nay')
print(scrape_any('https://www.datart.sk/notebook-apple-macbook-air-13-6-m2-8x-gpu-256gb-starlight-sk-mly13sl-a.html'), 'datart')
print(validate_url('https://www.alza.sk/hobby/konferencny-stolik-montana-130-70-cm-vyska-45-cm-podnozie-a-d7144761.htm'))
'''
