import sys
sys.path.append("/Users/kawamotoseiya/Library/Python/3.7/lib/python/site-packages")
import requests
from bs4 import BeautifulSoup

load_url = "https://reajoy.net/shingeki-new/31516/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

print(soup.find("title"))
