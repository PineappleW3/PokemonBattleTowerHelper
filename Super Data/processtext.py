import sqlite3

import os


dirname2 = os.path.dirname(__file__)
filename2 = os.path.join(dirname2, 'natures.csv')

f = open(filename2, "r")

def naturegather():
    naturelist = []
    while True:
        temp = f.readline()
        if len(temp)<3:
            return naturelist
        temp = temp.strip()
        temp = temp.split(",")
        for i in range(1,6):
            temp[i] = float(temp[i])
        naturelist.append(temp)