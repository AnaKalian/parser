import requests

from bs4 import BeautifulSoup

import csv

def get_html(url):
    r = requests.get (url)
    return r.text 


def get_all_links(html):
    soup = BeautifulSoup (html, 'lxml')
    
    tds =soup.find('table', id='currencies-all').find_all('td', class_='currency-name')

    links = []

    for td in tds:
        a = td.find('a').get('href')
        link = 'https://coinmarketcap.com' + a 
        links.append(link)
    return links
'''

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxsm')
    try: 
        name = soup.find('h1', class_='text-large').text.strip()
    except:
        name = ''
    try:
        price = soup.find('span',id='quote_price').text.strip()
    except:
        price = ''
    data = {'name':name, 'price':price }

    return data

def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow (data['name'],data['price'])
'''


def main():
    url ='https://coinmarketcap.com/all/views/all/'

    all_links = get_all_links(get_html(url))
    for i in all_links:
        print i




if __name__ == "__main__":
    main()