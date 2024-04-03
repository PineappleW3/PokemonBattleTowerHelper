from BonusInfo import *
from CalculateDamage import *
from ChangeStatus import *
from CreateOpponent import *
from CullOpponents import *
from GetItem import *
from GetLevel import *
from GetMoves import *
from ChooseSpecies import *
from GetAbility import *
from GetHP import *
import sys

import math
import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

from LoadTeam import *


def DataEntry():
    moves = []
    item = "Unknown"
    team = LoadTeam()
    teamoffset = 0
    opponententered = False
    bonus = [5,False,False,False]
    while True:
        if opponententered == False:
            species = ChooseSpecies()
            opponents = CreateOpponent(species)
            opponententered = True
        CullOpponents(opponents,item,moves)

        player = team[teamoffset]
        
        try:
            choice = int(input("\nWhat would you like to do? \n1)Change the opponent species \n2)Enter the moves used by the opponent \n3)Enter the item of the opponent \n4)Enter the status of either Pokemon \n5)Enter other information about the state of the battle \n6)Enter the HP of both Pokemon \n7)Enter the ability of the opponent Pokemon \n8)Change which one of your Pokemon is currently active \n9)Finish data entry \nPlease choose the number: "))
        except:
            choice = 100

        if choice == 1:
            choice2 = input("Are you sure? This will clear all previously entered information(Y/N) ")
            if choice2.title() == "Y":
                species = ChooseSpecies()
                opponents = CreateOpponent(species)

        elif choice == 2:
            moves.append(GetMoves(opponents))

        elif choice == 3:
            item = GetItem(opponents)

        elif choice == 4:
            temp = ChangeStatus(player,opponents)
            player = temp[0]
            opponents = temp[1]

        elif choice == 5:
            bonus = BonusInfo()

        elif choice == 6:
            temp = GetHP(player,opponents)
            player = temp[0]
            opponents = temp[1]

        elif choice == 7:
            opponents = GetAbility(opponents)

        elif choice == 8:
            try:
                temp = int(input("Which team slot would you like to switch to? "))
            except:
                temp = 6
            if temp < 1 or temp > 3:
                print("Invalid input")
            else:
                teamoffset = temp-1

        elif choice == 9:
            choice2 = input("Are you sure?(Y/N) ")
            if choice2.title() == "Y":
                return(team,teamoffset,opponents,bonus)

        else:
            print("Invalid input")

        team[teamoffset] = player

        
def GameplayLoop():
    temp = DataEntry()
    team = temp[0]
    offset = temp[1]
    opponents = temp[2]
    bonus = temp[3]


GameplayLoop()
