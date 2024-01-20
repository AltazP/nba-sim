import pandas as pd
from bs4 import BeautifulSoup
from geturl import find_url
from getData import getDF
import numpy as np
import requests
import os
import sys

url = find_url("Joel Embiid")
dataFrame = getDF(url)
current_year_column = dataFrame[dataFrame['Season'] == '2023-24'].index[0]
print(dataFrame)
