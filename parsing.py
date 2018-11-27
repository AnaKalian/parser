import requests

from bs4 import BeautifulSoup

import csv

def get_html(url):
    r = requests.get (url)
    return r.text 

def get_all_links(html):
    soup = BeautifulSoup (html, 'lxml')
    
    tds =soup.find('div', class_='news-list').find_all('div',class_ = 'news-line-item')

    links = []

    for td in tds:
        a = td.find('a').get('href')
        #link = 'https://coinmarketcap.com' + a 
        links.append(a)
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
    url ='https://pythondigest.ru/feed/'

    newfile = open('myfile.txt','w')
    all_links = get_all_links(get_html(url))
    for i in all_links:        
        newfile.write(i+'\n')
    newfile.close()




if __name__ == "__main__":
    main()