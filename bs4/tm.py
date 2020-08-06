import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


page = requests.get('https://vk.com/@yvkurse')
r = requests.get('http://github.com', allow_redirects=True)
bs4 = BeautifulSoup(page.content, 'html.parser')
#print (bs4.prettify())

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')
bs4_book = BeautifulSoup(html.read(), 'lxml')

nameList = bs4_book.findAll('span', {'class':'green'})
for name in nameList:
    print(name.get_text())

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs4_book = BeautifulSoup(html.read(), 'lxml') # html5lib
        #print (bs4_book.body)
        title = bs4_book.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)