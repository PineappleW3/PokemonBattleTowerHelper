import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

def SearchData():
    try:
        choice = int(input("What would you like to search for? \n1)Pokemon \n2)Move \n3)Item \n4)Ability \nPlease input the number: "))
    except:
        choice = 0


    if choice == 1:
        search = input("Please enter the Pokemon name: ")
        search = search.title()
        dataname = cursor.execute(
            "SELECT Type1,Type2,Abilities FROM PokemonSpecies WHERE Name = ?",
            (search,),
        ).fetchall()
        if len(dataname) > 0:
            type1 = dataname[0][0]
            type2 = dataname[0][1]
            abilities = dataname[0][2]
            abilities = abilities.split(",")

            ability2 = []
            for i in abilities:
                if i in ability2:
                    filler = 1
                else:
                    ability2.append(i)
            abilities = ability2

            if type2 != "None":
                print(search + " is a " + type1 + " and " + type2 + " type")
            else:
                print(search + " is a " + type1 + " type")
            print("These are its potential abilities: ")
            for i in abilities:
                print(i)

        else:
            print("Invalid input")

    elif choice == 2:
        search = input("Please enter the move name: ")
        search = search.title()
        dataname = cursor.execute(
            "SELECT Type,Category,Power,Accuracy,Description FROM Moves WHERE MoveName = ?",
            (search,),
        ).fetchall()
        if len(dataname) > 0:
            type1 = dataname[0][0]
            category = dataname[0][1]
            power = dataname[0][2]
            accuracy = dataname[0][3]
            description = dataname[0][4]
            if category != "Status":
                print(search + " is a " + type1 + " type " + category + " move, with " + str(power) + " power and " + str(accuracy) + " accuracy")
            else:
                print(search + " is a " + type1 + " type " + category + " move, with "  + str(accuracy) + " accuracy")
                print("It is described as: " + description)
            

        else:
            print("Invalid input")

    elif choice == 3:
        search = input("Please enter the item name: ")
        search = search.title()
        dataname = cursor.execute(
            "SELECT Description FROM Items WHERE ItemName = ?",
            (search,),
        ).fetchall()
        if len(dataname) > 0:
            description = dataname[0][0]
            print(search + " is described as: \n" + description)
        else:
            print("Invalid input")

    elif choice == 4:
        search = input("Please enter the item name: ")
        search = search.title()
        dataname = cursor.execute(
            "SELECT Description FROM Abilities WHERE AbilityName = ?",
            (search,),
        ).fetchall()
        if len(dataname) > 0:
            description = dataname[0][0]
            print(search + " is described as: \n" + description)
        else:
            print("Invalid input")

    else:
        print("Invalid input")