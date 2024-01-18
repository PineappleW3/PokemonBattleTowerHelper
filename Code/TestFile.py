from CreateTeam import *
from LoadTeam import *
from SaveTeam import *
from EditTeam import *


team2 = LoadTeam()

valid = False
while valid != "True":
    team3 = ChangeTeam(team2)
    valid = input(" ")

SaveTeam(team3)
