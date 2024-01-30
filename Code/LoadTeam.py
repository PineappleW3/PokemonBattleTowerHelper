from MainObject import *
import sqlite3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

def LoadTeam():
    filed = input("What is the name of the text file to open? ")
    #could probably do this check better
    if filed.find('.') == -1:
        filed = filed + ".txt"
    dirname = os.path.dirname(__file__)
    filed = os.path.join(dirname, filed)
    try:
        f = open(filed, "r")
    except:
        print("Could not find file")
        return LoadTeam()

    #there was definitely an easier way to do this
    Pokemon1 = Pokemon(f.readline().strip())
    Pokemon1.setitem(f.readline().strip())
    Pokemon1.setability(f.readline().strip())
    Pokemon1.sethp(f.readline().strip())
    Pokemon1.setattack(f.readline().strip())
    Pokemon1.setdefense(f.readline().strip())
    Pokemon1.setspatk(f.readline().strip())
    Pokemon1.setspdef(f.readline().strip())
    Pokemon1.setspeed(f.readline().strip())
    moves1 = [f.readline().strip(),f.readline().strip(),f.readline().strip(),f.readline().strip()]
    Pokemon1.setmoves(moves1)

    f.readline().strip()

    Pokemon2 = Pokemon(f.readline().strip())
    Pokemon2.setitem(f.readline().strip())
    Pokemon2.setability(f.readline().strip())
    Pokemon2.sethp(f.readline().strip())
    Pokemon2.setattack(f.readline().strip())
    Pokemon2.setdefense(f.readline().strip())
    Pokemon2.setspatk(f.readline().strip())
    Pokemon2.setspdef(f.readline().strip())
    Pokemon2.setspeed(f.readline().strip())
    moves2 = [f.readline().strip(),f.readline().strip(),f.readline().strip(),f.readline().strip()]
    Pokemon2.setmoves(moves2)

    f.readline().strip()

    Pokemon3 = Pokemon(f.readline().strip())
    Pokemon3.setitem(f.readline().strip())
    Pokemon3.setability(f.readline().strip())
    Pokemon3.sethp(f.readline().strip())
    Pokemon3.setattack(f.readline().strip())
    Pokemon3.setdefense(f.readline().strip())
    Pokemon3.setspatk(f.readline().strip())
    Pokemon3.setspdef(f.readline().strip())
    Pokemon3.setspeed(f.readline().strip())
    moves3 = [f.readline().strip(),f.readline().strip(),f.readline().strip(),f.readline().strip()]
    Pokemon3.setmoves(moves3)


    #assign types
    rows1 = cursor.execute(
        "SELECT Type1, Type2 FROM PokemonSpecies WHERE Name = ?",
        (Pokemon1.getname(),),
    ).fetchall()[0]
    Pokemon1.settype1(rows1[0])
    Pokemon1.settype2(rows1[1])

    rows2 = cursor.execute(
        "SELECT Type1, Type2 FROM PokemonSpecies WHERE Name = ?",
        (Pokemon2.getname(),),
    ).fetchall()[0]
    Pokemon2.settype1(rows2[0])
    Pokemon2.settype2(rows2[1])

    rows3 = cursor.execute(
        "SELECT Type1, Type2 FROM PokemonSpecies WHERE Name = ?",
        (Pokemon3.getname(),),
    ).fetchall()[0]
    Pokemon3.settype1(rows3[0])
    Pokemon3.settype2(rows3[1])


    team = [Pokemon1, Pokemon2, Pokemon3]
    f.close()
    return team


#=m]z(K2b72rl