import requests
from bs4 import BeautifulSoup

keyword = input("Search: ")
URL = "https://en.wikipedia.org/wiki/"
r = requests.get(URL + keyword)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
p1 = soup.select("#mw-content-text > div.mw-content-ltr.mw-parser-output > p:nth-child(7)")
print(f"Judul: {soup.title.string}")
print(p1)