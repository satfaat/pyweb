import requests
from bs4 import BeautifulSoup
#from urllib.request import urlopen

page = requests.get('https://vk.com/@yvkurse')
bs4 = BeautifulSoup(page.content, 'html.parser')
#print (bs4.prettify())

#weblinks = soup.find_all('a', {'class': 'author-page-article__href'})[0]
#print('my div =', weblinks)
#print(type(weblinks), len(weblinks))

urls = []
#for link in soup.find_all('a', {'class': 'author-page-article__href'}):
#    urls.append('https://vk.com' + link.get('href'))
#print(urls)

for link in bs4.find_all('a', {'class': 'author-page-article__href'}):
    if 'href' in link.attrs:
        #print(link.attrs['href'])
        print(link.attrs)
        urls.append('https://vk.com' + link.attrs['href'])
print(urls)

article1 = requests.get(urls[0])
soup1 = BeautifulSoup(article1.content, 'html.parser') # <class 'bs4.BeautifulSoup'>
content = soup1.find_all('div', {'class': 'articleView__content'}) # <class 'bs4.element.ResultSet'>
print (art_content.get_text())
for line in content:
    pass
    #print('line =', line.get_text())

article1 = requests.get(urls[0])
soup1 = BeautifulSoup(article1.content, 'html.parser') # <class 'bs4.BeautifulSoup'>
art_content = soup1.find_all('div', {'class': 'articleView__content'}) # <class 'bs4.element.ResultSet'>
print (art_content.prettify())

imgs = []
article1 = requests.get(ahrefs[0])
soup1 = BeautifulSoup(article1.content, 'html.parser') # <class 'bs4.BeautifulSoup'>
art_content = soup1.find_all('div', {'class': 'articleView__content'}) # <class 'bs4.element.ResultSet'>
img = soup1.findAll('img')
for link in soup1.find_all('img'):
    if 'src' in link.attrs:
        imgs.append(link.attrs['src'])
print (imgs)

articles = []
for i in range(len(urls)):
    content = BeautifulSoup(requests.get(urls[i]).content, 'html.parser').find_all('div', {'class': 'articleView__content'})
    for line in content:
        #print('line', i ,'=', line.get_text())
        articles.append(line.get_text())
print(articles)


# div class="article_layer__content"
#<div class="author-page-article">
#<a class="author-page-article__href" href="/@yvkurse-muzei-teatr-aleshino-podvore?context=author_page_date&amp;ref=author_page"></a>
# div class="layout"


#print('index =', weblinks[0])
#pagelinks = []

#for link in weblinks:
#    print (type(link))
    #url = link.contents[0].find_all('a')[0]   
    #pagelinks.append('https://vk.com/'+url.get('href'))
#print (pagelinks)


#for tag in soup.find_all(True):
#    print(tag.name)

#print(a.replace("H", "J"))
