import sqlite3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

dirname2 = os.path.dirname(__file__)
filename2 = os.path.join(dirname2, 'moves.csv')

f = open(filename2, "r", encoding= "UTF-8")


while True:
    poke = f.readline()
    if len(poke) < 10:
        break
    else:
        poke = poke.split(",")
        description = poke[2]

        
        bonus = len(poke) - 11
        if len(poke) > 11:
            count = 0
            while count != bonus:
                description = description + "," +  poke[count+3]
                count+=1
            description = description[1:]
            description = description[:-2]

        name = poke[1]
        type = poke[3+bonus]
        category = poke[4+bonus]
        power = poke[5+bonus]
        accuracy = poke[6+bonus]
        pp = poke[7+bonus]
        z = poke[8+bonus]
        priority = poke[9+bonus]
        crit = poke[10+bonus]

        

        try:
            cursor.execute("INSERT INTO Moves VALUES (?,?,?,?,?,?,?,?,?,?)",(name, type, category, power, accuracy, pp, priority, crit, z, description))
        except:
            uselessvar = 3

connection.commit()
connection.close()