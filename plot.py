import csv
import numpy as np
import matplotlib
from matplotlib import pylab as plt
from pylab import *

def print_game(GameID, p_reader):
    row_list = list(p_reader)
    #print(row_list)
    player = []
    for row in row_list:
        if row[0] == "0":
            player.append(row)
    print(player)


with open('player.csv', 'r') as playerfile:
    p_reader = csv.reader(playerfile)
    print_game(0, p_reader)
