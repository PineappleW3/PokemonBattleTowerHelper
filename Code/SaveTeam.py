from MainObject import *
import sqlite3

import os

def SaveTeam(team):
    filed = input("What would you like to name the file? ")
    if filed.find('.') == -1:
        filed = filed + ".txt"
    dirname = os.path.dirname(__file__)
    filed = os.path.join(dirname, filed)

    team1 = team[0]
    team2 = team[1]
    team3 = team[2]

    f = open(filed, "w")

    f.write(team1.getname())
    f.write("\n")
    f.write(team1.getitem())
    f.write("\n")
    f.write(team1.getability())
    f.write("\n")
    f.write(str(team1.gethp()))
    f.write("\n")
    f.write(str(team1.getattack()))
    f.write("\n")
    f.write(str(team1.getdefense()))
    f.write("\n")
    f.write(str(team1.getspatk()))
    f.write("\n")
    f.write(str(team1.getspdef()))
    f.write("\n")
    f.write(str(team1.getspeed()))
    f.write("\n")
    f.write(team1.getmoves()[0])
    f.write("\n")
    f.write(team1.getmoves()[1])
    f.write("\n")
    f.write(team1.getmoves()[2])
    f.write("\n")
    f.write(team1.getmoves()[3])
    f.write("\n")

    f.write("$\n")

    f.write(team2.getname())
    f.write("\n")
    f.write(team2.getitem())
    f.write("\n")
    f.write(team2.getability())
    f.write("\n")
    f.write(str(team2.gethp()))
    f.write("\n")
    f.write(str(team2.getattack()))
    f.write("\n")
    f.write(str(team2.getdefense()))
    f.write("\n")
    f.write(str(team2.getspatk()))
    f.write("\n")
    f.write(str(team2.getspdef()))
    f.write("\n")
    f.write(str(team2.getspeed()))
    f.write("\n")
    f.write(team2.getmoves()[0])
    f.write("\n")
    f.write(team2.getmoves()[1])
    f.write("\n")
    f.write(team2.getmoves()[2])
    f.write("\n")
    f.write(team2.getmoves()[3])
    f.write("\n")

    f.write("$\n")

    f.write(team3.getname())
    f.write("\n")
    f.write(team3.getitem())
    f.write("\n")
    f.write(team3.getability())
    f.write("\n")
    f.write(str(team3.gethp()))
    f.write("\n")
    f.write(str(team3.getattack()))
    f.write("\n")
    f.write(str(team3.getdefense()))
    f.write("\n")
    f.write(str(team3.getspatk()))
    f.write("\n")
    f.write(str(team3.getspdef()))
    f.write("\n")
    f.write(str(team3.getspeed()))
    f.write("\n")
    f.write(team3.getmoves()[0])
    f.write("\n")
    f.write(team3.getmoves()[1])
    f.write("\n")
    f.write(team3.getmoves()[2])
    f.write("\n")
    f.write(team3.getmoves()[3])

    
    f.close()
    return 5