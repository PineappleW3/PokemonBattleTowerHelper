import sqlite3
import math
from processtext import *
naturelist = naturegather()

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()


dirname2 = os.path.dirname(__file__)
filename2 = os.path.join(dirname2, 'willpower.html')

f = open(filename2, "r")
#f.readline()

def eraser(vari):
    vari = [*vari]
    removing = False
    new2 = ""
    for i in vari:
        if removing == False:
            if i == "<" or i == "&":
                removing = True
            else:
                new2 = new2 + i
        elif removing == True:
            if i == ">":
                removing = False
    vari = new2.strip()
    return vari

def naturestatthing(naturelist,nature):
    for i in naturelist:
        if i[0] == nature:
            naturestat = i
    
    return naturestat


count = 0
while True:
    count+=1

    #1
    if len(f.readline()) < 5:
        break

    #2
    f.readline()

    #3
    name = f.readline()
    name = eraser(name)

    #4
    f.readline()

    #5
    item = f.readline()
    item = eraser(item)

    #6
    f.readline()

    #7
    move1 = f.readline()
    move1 = eraser(move1)

    #8
    f.readline()

    #9
    move2 = f.readline()
    move2 = eraser(move2)

    #10
    f.readline()

    #11
    move3 = f.readline()
    move3 = eraser(move2)

    #12
    f.readline()

    #13
    move4 = f.readline()
    move4 = eraser(move2)

    #14
    f.readline()

    #15
    nature = eraser(f.readline())

    #16
    f.readline()

    #17
    temp = f.readline()
    if len(temp) > 10:
        hp = 1
    else:
        hp = 0
    
    #18
    f.readline()

    #19
    temp = f.readline()
    if len(temp) > 10:
        atk = 1
    else:
        atk = 0

    #20
    f.readline()

    #21
    temp = f.readline()
    if len(temp) > 10:
        defn = 1
    else:
        defn = 0

    #22
    f.readline()

    #23
    temp = f.readline()
    if len(temp) > 10:
        spa = 1
    else:
        spa = 0

    #24
    f.readline()

    #25
    temp = f.readline()
    if len(temp) > 10:
        spd = 1
    else:
        spd = 0

    #26
    f.readline()

    #27
    temp = f.readline()
    if len(temp) > 10:
        spe = 1
    else:
        spe = 0

    #28
    f.readline()

    #29
    f.readline()

    #30
    f.readline()

    #31
    f.readline()

    types = cursor.execute(
        "SELECT Type1, Type2 FROM PokemonSpecies WHERE Name = ?",
        (name,),
    ).fetchall()
    name2 = name
    if len(types)<1:
        print("The counter is at " + str(count))
        print("The Pokemon is " + name)
        name2 = input("What is the Pokemon name? ")
        types = cursor.execute(
            "SELECT Type1, Type2 FROM PokemonSpecies WHERE Name = ?",
            (name2,),
        ).fetchall()
    type1 = types[0][0]
    type2 = types[0][1]

    stats3 = cursor.execute(
         "SELECT Hp,Attack,Defense,SpAtk,SpDef,Speed FROM PokemonSpecies WHERE Name = ?",
         (name2,),
    ).fetchall()[0]
    #stat calculations
    naturestat = naturestatthing(naturelist,nature)
    HP1 = math.floor((((2*stats3[0]) + 31 + (63*hp))*50)/100) + 60
    Attack1 = math.floor((math.floor((((2*stats3[1]) + 31 + (63*atk))*50)/100)+5)*naturestat[1])
    Defense1 = math.floor((math.floor((((2*stats3[2]) + 31 + (63*defn))*50)/100)+5)*naturestat[2])
    Spa1 = math.floor((math.floor((((2*stats3[3]) + 31 + (63*spa))*50)/100)+5)*naturestat[3])
    Spd1 = math.floor((math.floor((((2*stats3[4]) + 31 + (63*spd))*50)/100)+5)*naturestat[4])
    Speed1 = math.floor((math.floor((((2*stats3[5]) + 31 + (63*spe))*50)/100)+5)*naturestat[5])


    cursor.execute("INSERT INTO Opponents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(count,name,item,move1,move2,move3,move4,HP1,Attack1,Defense1,Spa1,Spd1,Speed1,type1,type2,name2))


connection.commit()
connection.close()