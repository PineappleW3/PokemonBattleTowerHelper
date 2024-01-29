from MainObject import *
import sqlite3

#sorts out file name craziness
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()


def CreateTeam():
    team = []
    count = 0
    while count < 3:
        count +=1
        valid = False

        #loops until valid
        while valid == False:
            name = str(input("Enter the name of Pokemon number " + str(count) + " "))
            name = name.title()

            #tries to validate using database query for types
            rows = cursor.execute(
                "SELECT Type1, Type2 FROM PokemonSpecies WHERE Name = ?",
                (name,),
            ).fetchall()

            if len(rows) > 0:
                valid = True
            if valid == False:
                print ("Invalid Pokemon species name (try checking spelling)")

        #setting attributes       
        poke = Pokemon(name) 
        rows = rows[0]
        poke.settype1(rows[0])
        poke.settype2(rows[1])
        team.append(poke)
    return team