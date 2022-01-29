import csv

f = open("game.csv")
csv_f = csv.reader(f)
for row in csv_f:
    print('{:<6}  {:<6}  {:<6} {:<6} {:<6} {:<6} {:<6} {:<6}   {:<6}'.format(*row))

print('------------------------------------')

f = open("player.csv")
csv_f = csv.reader(f)
for row in csv_f:
    print('{:<6}  {:<6}  {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}'.format(*row))