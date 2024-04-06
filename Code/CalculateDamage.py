import math
import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

from LoadTeam import *


def CalculateDamage(attacker, defender, move, bonus):
    #necessary information on the move
    damagestuff = cursor.execute(
        "SELECT Category,Power,Type from Moves WHERE MoveName = ?",
        (move,),
    ).fetchall()[0]
    damagetype = damagestuff[0]
    power = damagestuff[1]
    movetype = damagestuff[2]

    #sets the attack and defense stats based on the type of move used
    if damagetype == "Physical":
        attack = attacker.getattack()
        defense = defender.getdefense()

    elif damagetype == "Special":
        attack = attacker.getspatk()
        if move == "Psyshock" or move == "Psystrike":
            defense = defender.getdefense()
        else:
            defense = defender.getspdef()

    elif damagetype == "Status":
        #message for later testing
        print("Things have gone awfully wrong somewhere")


    attack = int(attack)
    defense = int(defense)


    #VERY SCUFFED
    #LITERALLY JUST WRONG
    #NEED TO FIX LATER
    #PLEASE DONT FORGET TO DO THIS
    try:
        power = int(power)
    except:
        power = 50


    if bonus[0] == 3 and (defender.gettype1() == "Rock" or defender.gettype2 == "Rock") and damagetype == "Special" and (move != "Psyshock" and move != "Psystrike"):
        defense = round(defense*1.5)


    #initial calculation
    damage = 22*power*(attack/defense)
    damage = round((damage/50)+2)

    #rain
    if bonus[0] == 1:
        if movetype == "Fire":
            damage = round(damage/2)
        elif movetype == "Water":
            damage = round(damage*1.5)

    #sun
    if bonus[0] == 2:
        if movetype == "Water":
            damage = round(damage/2)
        elif movetype == "Fire":
            damage = round(damage*1.5)

    #random damage roll (using average)
    damage = round(damage*0.92)

    #STAB
    if movetype == attacker.gettype1() or movetype == attacker.gettype2():
        damage = round(damage*1.5)

    typeeffect = cursor.execute(
        "SELECT * from Typechart WHERE Type1 = ? AND Type2 = ?",
        (defender.gettype1(),defender.gettype2(),),
    ).fetchall()[0]

    if movetype == "Normal":
        index = 3
    elif movetype == "Fire":
        index = 4
    elif movetype == "Water":
        index = 5
    elif movetype == "Electric":
        index = 6
    elif movetype == "Grass":
        index = 7
    elif movetype == "Ice":
        index = 8
    elif movetype == "Fighting":
        index = 9
    elif movetype == "Poison":
        index = 10
    elif movetype == "Ground":
        index = 11
    elif movetype == "Flying":
        index = 12
    elif movetype == "Psychic":
        index = 13
    elif movetype == "Bug":
        index = 14
    elif movetype == "Rock":
        index = 15
    elif movetype == "Ghost":
        index = 16
    elif movetype == "Dragon":
        index = 17
    elif movetype == "Dark":
        index = 18
    elif movetype == "Steel":
        index = 19
    elif movetype == "Fairy":
        index = 20

    typething2 = typeeffect[index]
    damage = round(damage*typething2)


    return(damage)