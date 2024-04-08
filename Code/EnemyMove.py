import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

from CalculateDamage import *

def EnemyMove(team,offset,opponents,bonus):
    moveslist = []
    #loops for every opponent
    for i in opponents:
        attackmoves = []
        statusmoves = []
        moves = i.getmoves()

        #creates two lists of status and attacking moves
        for j in moves:
            damagestuff = cursor.execute(
                "SELECT Category from Moves WHERE MoveName = ?",
                (j,),
            ).fetchall()[0][0]
            if damagestuff == "Status":
                statusmoves.append(j)
            else:
                attackmoves.append(j)

        #find the damage of each attacking move
        attackvalues = []
        for j in attackmoves:
            damage = CalculateDamage(i,team[offset],j,bonus)
            damage = int(damage)
            attackvalues.append(damage)

        #finds the strongest move
        maxdamage = -1
        damageoffset = 0
        count = 0
        for j in attackvalues:
            if j > maxdamage:
                maxdamage = j
                damageoffset = count
            count+=1
        strongestmove = attackmoves[damageoffset]

        
        likelymoves = [[strongestmove,maxdamage],statusmoves]
        moveslist.append(likelymoves)
    return (moveslist)