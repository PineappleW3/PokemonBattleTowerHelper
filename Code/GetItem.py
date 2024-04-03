from MainObject import *
from CreateOpponent import *

import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

def GetItem(opponents):
    item = str(input("What item does the opponent have? "))
    item = item.title()

    #validation using the opponents list
    valid = False
    for i in opponents:
        temp = i.getitem()
        if temp == item:
            valid = True

    if valid == True:
        return item
    else:
        print("Item invalid for the current Pokemon species")
        return GetItem(opponents)
