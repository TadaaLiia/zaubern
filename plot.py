import csv
import numpy as np
import matplotlib
from matplotlib import pylab as plt
from pylab import *

def plot_game(GameID, p_reader):
    # list of rows
    row_list = list(p_reader)
    # list of GameID "0" -rows 
    player = []
    for row in row_list:
        if row[0] == "0":
            player.append(row)
    
    p0 = player[0]
    p1 = player[1]
    p2 = player[2]
    P0 = p0[2:22]
    P1 = p1[2:22]
    P2 = p2[2:22]
    print(P1)
    print(P2)
    print(P0)



with open('Zaubern/data/player.csv', 'r') as playerfile:
    p_reader = csv.reader(playerfile)
    plot_game(0, p_reader)
