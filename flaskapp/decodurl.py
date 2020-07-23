import urllib.parse

def encodurl (url):
    encoded = urllib.parse.quote(url)
    #decoded = urllib.parse.unquote(encoded)
    #result = encoded, ' = ', decoded
    return encoded

def decodurl(url):
    decoded = urllib.parse.unquote(url)
    return decoded