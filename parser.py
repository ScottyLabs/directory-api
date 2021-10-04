import requests
from bs4 import BeautifulSoup as bs

payload = {'search': 'ghyppoli', 'action': 'Search', 'searchtype': 'basic', 'activetab': 'basic'}

r = requests.post("https://directory.andrew.cmu.edu/index.cgi", data=payload)

soup = bs(r.text, 'html.parser')
result = soup.find('div', style="padding-top: 50px;")

# print(soup.find('h1', id="listing").text)
print(result.h1.text)
info = result.p.contents
print(info[1][1:])
print(info[4][1:])
print(info[7][1:])
print(info[11].text)
