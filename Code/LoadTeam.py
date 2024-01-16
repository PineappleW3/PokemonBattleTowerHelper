from MainObject import *

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

    ##Sort out type thing when databases are made

    team = [Pokemon1, Pokemon2, Pokemon3]
    f.close()
    return team