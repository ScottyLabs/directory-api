import requests
from bs4 import BeautifulSoup as bs

payload = {'first_name': "Gael",
               'last_name': "Hyppolite",
               'andrew_id': None,
               'email': None,
               'action': 'Search',
               'searchtype': 'advanced',
               'activetab': 'advanced'}

r = requests.post("https://directory.andrew.cmu.edu/index.cgi", data=payload)
f = open("results.html", "w")
f.write(r.text)
f.close()

soup = bs(r.text, 'html.parser')
marker = soup.find('span', id="results_marker")
result = marker.findNext('div')
print(type(result))

# print(soup.find('h1', id="listing").text)
print(result.h1.text)
info = result.p.contents
print(info[1][1:])
print(info[4][1:])
print(info[7][1:])
print(info[11].text)
