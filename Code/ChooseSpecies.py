import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()


def ChooseSpecies():
	species = input("Enter the name of the enemy Pokemon species ")
	species = species.title()
	valid = False
	
    #validates that Pokemon appears in Opponents table
	item = cursor.execute(
        "SELECT Item FROM Opponents WHERE Name = ?",
        (species,),
    ).fetchall()
	if len(item) < 1:
		print ("Invalid Pokemon species name (try checking spelling)")
		species = ChooseSpecies()
		

	return (species)