import urllib.request, re, csv, html
from urllib.parse import urlparse

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def parse_with_regular_expressions(url, csv_filename):
    parserd_url = urlparse(url)
    site_scheme = parserd_url.scheme
    site_url = parserd_url.netloc
    response = urllib.request.urlopen(url)
    with open(csv_filename, 'w', encoding='utf-8', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        articles_urls = re.findall(r'<div class=\"author-page-article\">\s*<a href=\"(.+)\?', response.read().decode('utf-8'))

        for article_url in articles_urls:
            response = urllib.request.urlopen(f'{site_scheme}://{site_url}/{article_url}')
            article_html = response.read().decode('utf-8')
            title = re.findall(r'<h1\s*class=\"article_decoration_first article_decoration_last\"\s*>(.+)<span class=\'article_anchor_button\'', article_html)
            text = re.findall(r'<p\s*class=\"article_decoration_first article_decoration_last article_decoration_before\"\s*>(.+)</p>', article_html)
            text = html.unescape(cleanhtml(''.join(text)))
            image_urls = re.findall(r'<img.*article_carousel_img.*src=\"([^\"]+)\"', article_html)
            spamwriter.writerow([title] + [text] + image_urls)

parse_with_regular_expressions('https://vk.com/@yvkurse', 'output.csv')