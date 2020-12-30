import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup.p.string)