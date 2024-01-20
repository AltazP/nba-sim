import pandas as pd
from bs4 import BeautifulSoup
from geturl import find_url
import numpy as np
import requests
import os
import sys

def getDF(url):
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
    # print(charts[adv_num].text)

    # empty list
    data = []
    
    # for getting the header from
    # the HTML file
    list_header = []
    header = charts[adv_num].find("tr")
    
    for items in header:
        try:
            list_header.append(items.get_text())
        except:
            continue
    
    # for getting the data 
    HTML_data = charts[adv_num].find_all("tr")[1:]
    
    for element in HTML_data:
        sub_data = []
        for sub_element in element:
            try:
                sub_data.append(sub_element.get_text())
            except:
                continue
        data.append(sub_data)
    
    # Storing the data into Pandas
    # DataFrame 
    df = pd.DataFrame(data = data, columns = list_header).drop('\n',axis=1)
    return df
