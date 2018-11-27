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


def main():
    url ='https://pythondigest.ru/feed/'

    newfile = open('myfile.txt','w')
    all_links = get_all_links(get_html(url))
    for i in all_links:        
        newfile.write(i+'\n')
    newfile.close()




if __name__ == "__main__":
    main()