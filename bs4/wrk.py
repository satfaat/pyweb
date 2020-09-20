import requests, csv
from bs4 import BeautifulSoup as bs4

url = 'http://tdserebro.ru/samara/search'

page = requests.get(url)
bs = bs4(page.content, 'lxml')
ids = []
for line in bs.find_all('p', {'class': 'articleProduct'}):
    ids.append(line.get_text())
print(len(ids))
print(ids)