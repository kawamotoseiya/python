import sys
sys.path.append("/Users/kawamotoseiya/Library/Python/3.7/lib/python/site-packages")
import requests

url = "https://www.ymori.com/books/python2nen/test.html"

response = requests.get(url)

response.encoding = response.apparent_encoding

print(response.text)


