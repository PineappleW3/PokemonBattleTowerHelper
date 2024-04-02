from MainObject import *

import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

def CreateOpponent(species):
    #gets every potential opponent of a given Pokemon Species
    opponentstats = cursor.execute(
        "SELECT Item,Move1,Move2,Move3,Move4,HP,Attack,Defense,SpAtk,SpDef,Speed,Type1,Type2 FROM Opponents WHERE Name = ?",
        (species,),
    ).fetchall()

    #adds information into objects, and then appends all to a list
    enemylist = []
    for i in opponentstats:
        temp = Pokemon(species)
        temp.settype1(i[11])
        temp.settype2(i[12])
        temp.setitem(i[0])
        temp.setability("Unknown")
        temp.sethp(i[5])
        temp.setattack(i[6])
        temp.setdefense(i[7])
        temp.setspatk(i[8])
        temp.setspdef(i[9])
        temp.setspeed(i[10])
        moves = i[1:5]
        temp.setmoves(moves)
        enemylist.append(temp)

    return enemylist
