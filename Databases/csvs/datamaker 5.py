import sqlite3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

dirname2 = os.path.dirname(__file__)
filename2 = os.path.join(dirname2, 'type-chart.csv')

f = open(filename2, "r", encoding= "UTF-8")

count = 0
while True:
    poke = f.readline()
    if len(poke) < 10:
        break
    else:
        poke = poke.split(",")
        count+=1
        type1 = poke[0]
        type1 = type1.title()
        type2 = poke[1]
        if type2 == "":
            type2 = "None"
        type2 = type2.title()
        normal = poke[2]
        fire = poke[3]
        water = poke[4]
        electric = poke[5]
        grass = poke[6]
        ice = poke[7]
        fighting = poke[8]
        poison = poke[9]
        ground = poke[10]
        flying = poke[11]
        psychic = poke[12]
        bug = poke[13]
        rock = poke[14]
        ghost = poke[15]
        dragon = poke[16]
        dark = poke[17]
        steel = poke[18]
        fairy = poke[19]


        
        

        

        try:
            cursor.execute("INSERT INTO Typechart VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(count,type1,type2,normal,fire,water,electric,grass,ice,fighting,poison,ground,flying,psychic,bug,rock,ghost,dragon,dark,steel,fairy ))
        except:
            uselessvar = 3

connection.commit()
connection.close()