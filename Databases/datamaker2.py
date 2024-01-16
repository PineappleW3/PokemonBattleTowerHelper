import sqlite3

connection = sqlite3.connect("aquarium.db")
cursor = connection.cursor()

f = open("movesets.txt", "r", encoding= "unicode_escape")


while True:
    poke = f.readline()
    if len(poke) < 10:
        break
    else:
        poke = poke.split(",")
        name = poke[2]
        moveset = ""
        for i in range(1,175):
            move = poke[i+2]
            if len(move) > 2:
                place = move.index("-")
                move = move[place+2:len(move)]
                moveset = moveset + "," + move
        moveset = moveset[1:len(moveset)]
            
        try:
            cursor.execute("UPDATE PokemonSpecies SET Moveset = ? WHERE Name = ?",(moveset, name))
        except:
            print(name)

connection.commit()
connection.close()
input()