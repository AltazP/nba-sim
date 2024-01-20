from cont import cont
from getData import *
from random import random
import os

os.system('clear')
print("Welcome to Altaz's NBA Game Simulator")
print("You will have to pick 5 current players for each team.")
cont()
t1_urls = []
t2_urls = []

'''
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
'''
# Top one gets all players for first team then all players for second
# Bottom goes back and forth
p = 1
while p < 6:
    p1 = input(f"(Team 1) Player {p}: ")
    print("Getting Data..")
    url = find_url(p1)
    if len(url) == 0:
        print ("Player not found  (player must be current and capitalized correctly). Try again.")
        continue
    t1_urls.append(url[0])
    p1 = input(f"(Team 2) Player {p}: ")
    print("Getting Data..")
    url = find_url(p1)
    if len(url) == 0:
        print ("Player not found  (player must be current and capitalized correctly). Try again.")
        continue
    t2_urls.append(url[0])
    p += 1

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

t1_score = int(round(pred_score(t1_avg_per, t2_defense)))
t2_score = int(round(pred_score(t2_avg_per, t1_defense)))

winner = 0
if t1_score > t2_score:
    winner = 1
elif t2_score > t1_score:
    winner = 2
else:
    tiebreaker = random()
    if tiebreaker == 0:
        t1_score += 1
        winner = 1
    else:
        t2_score += 1
        winner = 2
print ('Final Score')
print('-------------')
print(f'Team 1: {t1_score}')
print(f'Team 2: {t2_score}')
print('-------------')
print(f'\nTEAM {winner} WINS!')