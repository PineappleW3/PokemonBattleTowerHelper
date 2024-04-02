import math
import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()


def CalculateDamage(attacker, defender, move, bonus):
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

    if bonus[0] == 3 and (defender.gettype1() == "Rock" or defender.gettype2 == "Rock") and damagetype == "Special" and (move != "Psyshock" and move != "Psystrike"):
        defense = round(defense*1.5)

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

    return("Still not over")



#CalculateDamage(1,1,"Thunderbolt",1)
