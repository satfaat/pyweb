import requests, csv
from bs4 import BeautifulSoup

url_from = 'https://vk.com/@yvkurse'

def grab_urls(url_from): # Получим список ссылок на статьи
    page = requests.get(url_from)
    bs4 = BeautifulSoup(page.content, 'lxml')
    #print(bs4.original_encoding)
    ahrefs = []
    for link in bs4.find_all('a', {'class': 'author-page-article__href'}):
        if 'href' in link.attrs:
            ahrefs.append('https://vk.com' + link.attrs['href'])
    return ahrefs
#print(grab_urls(url_from))

ahrefs = grab_urls(url_from)

def get_articles_from_urls(ahrefs): # Получим сами статьи и запишем их в лист
    articles = []
    for i in range(len(ahrefs)):
        content = BeautifulSoup(requests.get(ahrefs[i]).content, 'html.parser').find_all('div', {'class': 'articleView__content'})
        for line in content:
            if 'src' in line.attrs:
                articles.append(line.attrs['src'])
            else:
                articles.append(line.get_text())
    return articles
print(get_articles_from_urls(ahrefs))


# Запишем статьи в csv C:\Python38\lib\encodings\cp1251.py" encoding='utf-8'

articles = get_articles_from_urls(ahrefs)

def write_to_csv(articles):
    with open('datacsv/articles.csv', 'w', encoding='utf-8') as csvfile: #
        writer = csv.writer(csvfile) #  delimiter = '*'
        writer.writerow(articles)