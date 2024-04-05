#lmao you gotta do this in the future i can just play fortnite
#sucks to be you

#motherfucker

import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

def RankMoves(team,offset,opponents,bonus,expectedmoves):
    player = team[offset]
    playerhp = player.getcurrenthp()
    if playerhp == "Max":
        playerhp = player.gethp()
    ohkolist = []
    ohko = False
    for i in range (0,len(expectedmoves)):
        temp = expectedmoves[i]
        if temp[1] > playerhp:
            ohko = True
            ohkolist.append(i)

    outspeed = False
    for i in ohkolist:
        enemy = opponents[i]
        if enemy.getspeed()>player.getspeed():
            outspeed = True

    


