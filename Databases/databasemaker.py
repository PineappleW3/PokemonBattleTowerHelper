import sqlite3

connection = sqlite3.connect("aquarium.db")
cursor = connection.cursor()

f = open("pokemon.txt", "r", encoding= "unicode_escape")


while True:
    poke = f.readline()
    if len(poke) < 10:
        break
    else:
        poke = poke.split(",")
        name = poke[3]
        type1 = poke[4].title()
        type2 = poke[5]
        if len(type2) < 2:
            type2 = "none"
        type2 = type2.title()
        hp = poke[9]
        attack = poke[10]
        defense = poke[11]
        spatk = poke[12]
        spdef = poke[13]
        speed = poke[14]
        ability1 = poke[6]
        ability2 = poke[7]
        ability3 = poke[8]
        if len(ability2)>2:
            ability1 = ability1 + "," + ability2
        if len(ability3)>2:
            ability1 = ability1 + "," + ability3
        abilitystring = ability1
        try:
            cursor.execute("INSERT INTO PokemonSpecies VALUES (?,?,?,?,?,?,?,?,?,?,'Blank')",(name,type1,type2,hp,attack,defense,spatk,spdef,speed,abilitystring))
        except:
            sex = 3

connection.commit()
connection.close()