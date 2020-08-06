from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
#print(bs.body)
#for child in bs.find('table',{'id':'giftList'}).children:
    #print('this child of table', child)

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print('this sibling =', sibling)