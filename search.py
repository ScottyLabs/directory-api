import requests
from bs4.element import Tag
from bs4 import BeautifulSoup as bs

directory = "https://directory.andrew.cmu.edu/index.cgi"

def basic(query: str) -> Tag :
    payload = {'search': query,
               'action': 'Search',
               'searchtype': 'basic',
               'activetab': 'basic'}
    r = requests.post(directory, data = payload)
    soup = bs(r.text, 'html.parser')
    marker = soup.find('span', id="results_marker")
    return marker.findNext('div')

def advanced(fName: str, lName: str, aId: str, email: str) -> Tag :
    payload = {'first_name': fName,
               'last_name': lName,
               'andrew_id': aId,
               'email': email,
               'action': 'Search',
               'searchtype': 'advanced',
               'activetab': 'advanced'}
    r = requests.post(directory, data = payload)
    soup = bs(r.text, 'html.parser')
    marker = soup.find('span', id="results_marker")
    return marker.findNext('div')
