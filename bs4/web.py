import requests
from bs4 import BeautifulSoup
# -urllib3

page = requests.get('https://vk.com/@yvkurse')
soup = BeautifulSoup(page.content, 'html.parser')
#print (soup.prettify())

#weblinks = soup.find_all('a', {'class': 'author-page-article__href'})[0]
#print('my div =', weblinks)
#print(type(weblinks), len(weblinks))

weblinks_href = []
urls = []
for link in soup.find_all('a'):
    urls = []
    urls = urls.append(link.get('href'))
    #weblinks_href.append('https://vk.com/'+url.get('href'))
    #weblinks_href.append(lnk_list)
print(urls)




# div class="article_layer__content"
#<div class="author-page-article">
#<a class="author-page-article__href" href="/@yvkurse-muzei-teatr-aleshino-podvore?context=author_page_date&amp;ref=author_page"></a>



#print('index =', weblinks[0])
#pagelinks = []

#for link in weblinks:
#    print (type(link))
    #url = link.contents[0].find_all('a')[0]   
    #pagelinks.append('https://vk.com/'+url.get('href'))
#print (pagelinks)


#for tag in soup.find_all(True):
#    print(tag.name)
