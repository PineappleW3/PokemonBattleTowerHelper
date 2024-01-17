from MainObject import *
import sqlite3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

def LoadTeam():
    filed = input("What is the name of the text file to open? ")
    if filed.find('.') == -1:
        filed = filed + ".txt"
    f = open(filed, "r")

    Pokemon1 = Pokemon(f.readline())
    Pokemon1.setitem(f.readline())
    Pokemon1.setability(f.readline())
    Pokemon1.sethp(f.readline())
    Pokemon1.setattack(f.readline())
    Pokemon1.setdefense(f.readline())
    Pokemon1.setspatk(f.readline())
    Pokemon1.setspdef(f.readline())
    Pokemon1.setspeed(f.readline())
    moves1 = [f.readline(),f.readline(),f.readline(),f.readline()]
    Pokemon1.setmoves(moves1)

    f.readline()

    Pokemon2 = Pokemon(f.readline())
    Pokemon2.setitem(f.readline())
    Pokemon2.setability(f.readline())
    Pokemon2.sethp(f.readline())
    Pokemon2.setattack(f.readline())
    Pokemon2.setdefense(f.readline())
    Pokemon2.setspatk(f.readline())
    Pokemon2.setspdef(f.readline())
    Pokemon2.setspeed(f.readline())
    moves2 = [f.readline(),f.readline(),f.readline(),f.readline()]
    Pokemon2.setmoves(moves2)

    f.readline()

    Pokemon3 = Pokemon(f.readline())
    Pokemon3.setitem(f.readline())
    Pokemon3.setability(f.readline())
    Pokemon3.sethp(f.readline())
    Pokemon3.setattack(f.readline())
    Pokemon3.setdefense(f.readline())
    Pokemon3.setspatk(f.readline())
    Pokemon3.setspdef(f.readline())
    Pokemon3.setspeed(f.readline())
    moves3 = [f.readline(),f.readline(),f.readline(),f.readline()]
    Pokemon3.setmoves(moves3)

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