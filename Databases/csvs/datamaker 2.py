import sqlite3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

dirname2 = os.path.dirname(__file__)
filename2 = os.path.join(dirname2, 'items.csv')

f = open(filename2, "r", encoding= "UTF-8")


while True:
    poke = f.readline()
    if len(poke) < 10:
        break
    else:
        poke = poke.split(",")
        itemname = poke[1]
        description = poke[2]

        if len(poke) > 3:
            count = 3
            while count != len(poke):
                description = description + "," +  poke[count]
                count+=1
            description = description[1:]
            description = description[:-2]

        try:
            cursor.execute("INSERT INTO Items VALUES (?,?)",(itemname, description))
        except:
            uselessvar = 3

connection.commit()
connection.close()

