from MainObject import *
from CreateOpponent import *

import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

def GetMoves(opponents):
    move = str(input("What move has the opponent used? "))
    move = move.title()

    #special check since U-turn is the only move in the game to not capitalise the word after the hyphen
    if move == "U-Turn":
        move = "U-turn"

    #validation using the opponents list
    valid = False
    for i in opponents:
        temp = i.getmoves()
        
        for j in temp:
            if j == move:
                valid = True

    if valid == True:
        return move
    else:
        print("Move invalid for the current Pokemon species")
        return GetMoves(opponents)