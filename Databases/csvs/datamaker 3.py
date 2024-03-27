import sqlite3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

dirname2 = os.path.dirname(__file__)
filename2 = os.path.join(dirname2, 'abilities.csv')

f = open(filename2, "r", encoding= "UTF-8")


while True:
    poke = f.readline()
    if len(poke) < 10:
        break
    else:
        poke = poke.split(",")
        abilityname = poke[0].strip()
        description = poke[1]

        if len(poke) > 2:
            count = 2
            while count != len(poke):
                description = description + "," +  poke[count]
                count+=1
            description = description[1:]
            description = description[:-2]
        description = description.strip()
        try:
            cursor.execute("INSERT INTO Abilities VALUES (?,?)",(abilityname, description))
        except:
            uselessvar = 3

connection.commit()
connection.close()