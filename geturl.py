from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def find_url(name):
    
    page = urlopen('https://basketball.realgm.com/nba/players')
    soup = BeautifulSoup(page, "lxml")
    prefix = 'https://basketball.realgm.com'
    l = []
    name = name.replace(' ', '-')
    
    link = soup.find_all(href=re.compile(name))
    if len(link)>0 and ( len(link[0]) > 0 ):
        l.append(prefix + link[0]['href'])
    return l