from MainObject import *
from CreateOpponent import *

import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

def GetAbility(opponents):
    ability = str(input("What ability does the opponent have? "))
    ability = ability.title()

    dataname = cursor.execute(
        "SELECT DatabaseName FROM Opponents WHERE Name = ?",
        (opponents[0].getname(),),
    ).fetchall()[0][0]

    #validation using the database
    abilitychoices = cursor.execute(
        "SELECT Abilities FROM PokemonSpecies WHERE Name = ?",
        (dataname,),
    ).fetchall()[0][0]


    valid = False
    abilitychoices = abilitychoices.strip()
    abilitychoices = abilitychoices.split(",")
    if ability in abilitychoices:
        valid = True
    newopponents = []
    if valid == True:
        for i in opponents:
            i.setability(ability)
            newopponents.append(i)
        opponents = newopponents
        return (opponents)
    else:
        print("Ability invalid for the current Pokemon species")
        return GetAbility(opponents)
