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

from CalculateDamage import *

def RankMoves(team,offset,opponents,bonus,expectedmoves):
    player = team[offset]
    playerhp = player.getcurrenthp()
    ohkolist = []
    ohko = False
    for i in range (0,len(expectedmoves)):
        temp = expectedmoves[i]
        if temp[0][1] > playerhp:
            ohko = True
            ohkolist.append(i)

    

    attackmoves2 = []
    statusmoves2 = []
    moves = player.getmoves()
    for j in moves:
        damagestuff = cursor.execute(
            "SELECT Category from Moves WHERE MoveName = ?",
            (j,),
        ).fetchall()[0][0]
        if damagestuff == "Status":
            statusmoves2.append(j)
        else:
            attackmoves2.append(j)
    attackvalues = []
    for j in attackmoves2:
        damage = CalculateDamage(player,opponents[0],j,bonus)
        damage = int(damage)
        attackvalues.append(damage)
    maxdamage = -1
    damageoffset = 0
    count = 0
    for j in attackvalues:
        if j > maxdamage:
            maxdamage = j
            damageoffset = count
        count+=1
    strongestmove = attackmoves2[damageoffset]

    #right now we know:
    #can the player be knocked out in one hit
    #which of the players attacks will deal the most damage

    strategy = "Attack"
    reason = "Filler"
    outspeedko = True
    for i in ohkolist:
        enemy = opponents[i]
        damage7 = CalculateDamage(player,enemy,strongestmove,bonus)
        
        if damage7 > enemy.getcurrenthp():
            if player.getspeed() > enemy.getspeed():
                filler = 7
                
        else:
            outspeedko = False
    
    if ohko == True and outspeedko == True:
        strategy = "Attack"
        reason = "The enemy can knock you out in one hit, but your Pokemon is faster and can knock the opponent out first"
        return[strategy,reason,strongestmove,maxdamage]
    elif ohko == True and outspeedko == False:
        strategy = "Switch"
        reason = "The opponent can knock you out in one hit before your Pokemon even has a chance to move"
        return[strategy,reason,strongestmove,maxdamage]
    
    ohkoenemy = True
    for i in opponents:
        enemy = i
        damage7 = CalculateDamage(player,enemy,strongestmove,bonus)
        if damage7 < enemy.getcurrenthp():
            ohkoenemy = False
    if ohkoenemy == True:
        strategy = "Attack"
        reason = "You are able to knock out the enemy in one hit"
        return[strategy,reason,strongestmove,maxdamage]
    else:
        strategy = "Anything"
        reason = "Neiter you or your opponent can knock each other out in one hit, so any move is fine"
        return[strategy,reason,strongestmove,maxdamage]
        

    


