from bs4 import BeautifulSoup
import requests, re, csv

link = 'https://vk.com/@yvkurse'
def link_parser(link):
    link_list = []
    response = requests.get(link)
    parse_result = BeautifulSoup(response.text, 'lxml')
    for link in parse_result.find_all('a', {'class': 'author-page-article__href'}):
        #link_list.append(link.get('href'))
        link_list.append(re.search(r'(.+)\?',('https://vk.com' + link.get('href'))).group(0)) #.group(0)
    return set(link_list)
    #return link_list
#print (link_parser(link))

def article_parser(link_list):
    arr=[]
    with open('datacsv/parse_result.csv', 'w') as f:
        
        writer = csv.writer(f)
        for link in link_list:
            response = requests.get(link+'UTF-8')
            parse_result = BeautifulSoup(response.text, 'lxml')
            #arr.append(parse_result)
            for text_article in parse_result.find_all('p', {'class': 'article_decoration_first'}):
                text = str(text_article)
                utf_text = text.encode(encoding="utf-8", errors="ignore")
                #print(re.sub('<[A-z/][^>]*>', '', utf_text.decode("utf-8")))
                writer.writerow(re.sub('<[A-z/][^>]*>', '', utf_text.decode("utf-8")))
    #return arr
print (article_parser(link_parser('https://vk.com/@yvkurse')))


def article_parser1(link_list):
        for link in link_list:
            response = requests.get(link)
            parse_result = BeautifulSoup(response.text, features='html.parser')
            ret = parse_result.get_text()
            nret = ret.split('\n')
            ret = ''.join(nret)
            print(''*5,'Text article: ',ret,'\n')
            i = 1
            for link in parse_result.select(".article_full_view__image"):
                print(link.get('src'), i)
                i += 1