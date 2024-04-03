from BonusInfo import *
from CalculateDamage import *
from ChangeStatus import *
from CreateOpponent import *
from CullOpponents import *
from GetItem import *
from GetLevel import *
from GetMoves import *
from ChooseSpecies import *
from GetAbility import *
from GetHP import *
import sys

import math
import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()

ChooseSpecies()