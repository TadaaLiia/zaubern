import csv

with open('game.csv') as gamefile:
    csv_g = csv.reader(gamefile)
    for row in csv_g:
        print('{:<6}  {:<6}  {:<6} {:<6} {:<6} {:<6} {:<6} {:<6}   {:<6}'.format(*row))


print('------------------------------------')

with open('player.csv', 'r') as playerfile:
    p_reader = csv.reader(playerfile)
    for row in p_reader:
        print('{:<6}  {:<6}  {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}'.format(*row))
