from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs4_book = BeautifulSoup(html.read(), 'lxml')
print(bs4_book.html)

nameList = bs4_book.findAll('span', {'class':'green'})
#.find_all('span', {'class':{'green', 'red'}}) = bs.find_all('', {'class':'green'})
#.find_all(['h1','h2','h3','h4','h5','h6'])
#title = bs.find_all(id='title', class_='text')
# bs.find_all(id='text') = bs.find_all('', {'id':'text'})
for name in nameList:
    print('span text', name.get_text())