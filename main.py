import pandas as pandas
from bs4 import BeautifulSoup
from geturl import find_url
import requests

url = find_url("Stephen Curry")

player_text = requests.get(url[0]).text
soup = BeautifulSoup(player_text, 'lxml')
charts = soup.find_all('table')

adv_num = 0
for i in range (0, len(charts)):
    adv = charts[i].find('tr', class_ = 'advanced_stats')
    if adv is None:
        continue
    else:
        adv_num = i
        break
print(charts[adv_num])