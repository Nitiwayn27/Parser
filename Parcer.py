# coding: utf8
import requests
from bs4 import BeautifulSoup

def save():
    with open ('parse_info.txt', 'a', encoding='utf-8') as file:
        file.write(f'{comp["title"]} -> Price: {comp["price"]} -> Link: {comp["link"]}\n')
def parse():
    URL='https://www.avito.ru/moskva_i_mo?q=PS+4'
    HEADERS = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.1.195 Yowser/2.5 Safari/537.36'

    }
    response = requests.get(URL, headers= HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div',class_='snippet-horizontal')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('a', class_= 'snippet-link').get_text(strip = True),
            'price': item.find('span', class_='snippet-price').get_text(strip=True),
            'link': item.find('a',class_= 'snippet-link' ).get('href')
        })
        global comp
        for comp in comps:
            print(f'{comp["title"]} -> Price: {comp["price"]} -> Link: {comp["link"]}')
            save()
parse()