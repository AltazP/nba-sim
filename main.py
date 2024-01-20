import pandas as pandas
from bs4 import BeautifulSoup
from geturl import find_url
import requests

url = find_url("Stephen Curry")

player_text = requests.get(url[0]).text
soup = BeautifulSoup(player_text, 'lxml')
charts = soup.find_all('table', class_ = 'tablesaw compact tablesaw-swipe tablesaw-sortable')

print(charts)