import pandas as pd
from bs4 import BeautifulSoup
from geturl import find_url
from cont import cont
from getData import *
import numpy as np
import requests
import os
import sys

'''
url = find_url("Joel Embiid")[0]
dataFrame = getDF(url)
current_year_column = dataFrame[dataFrame['Season'] == '2023-24'].index[0]
print(dataFrame)
'''
print("Welcome to Altaz's NBA Game Simulator")
print("You will have to pick 5 current players for each team.")
cont()
t1_urls = []
t2_urls = []
for t in range(1,3):
    p = 1
    while p < 6:
        p1 = input(f"(Team {t}) Player {p}: ")
        print("Getting Data..")
        url = find_url(p1)
        if len(url) == 0:
            print ("Player not found  (player must be current and capitalized correctly). Try again.")
        else:
            p += 1
            if t == 1:
                t1_urls.append(url[0])
            else:
                t2_urls.append(url[0])
print("\nAll Players Found!")
cont()
t1_avg_per = 0
t2_avg_per = 0
t1_defense = 0
t2_defense = 0
for p in t1_urls:
    df = getDF(p)
    t1_avg_per += getPER(df)
    t1_defense += getDRtg(df)
for p in t2_urls:
    df = getDF(p)
    t2_avg_per += getPER(df)
    t2_defense += getDRtg(df)
t1_avg_per /= 5
t1_defense /= 5
t2_avg_per /= 5
t2_defense /= 5