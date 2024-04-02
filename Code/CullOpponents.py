from MainObject import *
from CreateOpponent import *

import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

def CullOpponents(opponents, item, moves):
    newopponents = []

    for i in opponents:
        valid = True
        #gets the item and moveset of each Pokemon in the list
        tempitem = i.getitem()
        tempmoves = i.getmoves()

        #checks to see if the item matches only if an item has been set
        if tempitem != item and item != "Unknown":
            valid = False

        #checks to see if the moves are valid only if the list contains items
        if len(moves) > 0:
            for j in moves:
                if j not in tempmoves:
                    valid = False
        if valid == True:
            newopponents.append(i)

    return newopponents