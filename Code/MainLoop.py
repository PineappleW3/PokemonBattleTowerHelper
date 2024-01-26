from CreateTeam import *
from LoadTeam import *
from SaveTeam import *
from EditTeam import *

print("Welcome to the Pokemon battle tower helper")
teamloaded = False

while True:
    try:
        choice = int(input("What would you like to do?\n1)Create a new team\n2)Load an existing team\n3)Edit the currently loaded team\n4)Save the currently loaded team\n5)Close the program\nPlease input the number:"))
    except:
        choice = "Beans"

    if choice == 1:
        if teamloaded == True:
            choice2 = input("Are you sure? This will erase the currently loaded team (Y/N)")
            if choice2.upper() == "Y":
                team = CreateTeam()
                teamloaded = True
        else:
            team = CreateTeam()
            teamloaded = True

    elif choice == 2:
        if teamloaded == True:
            choice2 = input("Are you sure? This will erase the currently loaded team (Y/N)")
            if choice2.upper() == "Y":
                team = LoadTeam()
                teamloaded = True
        else:
            team = LoadTeam()
            teamloaded = True

    elif choice == 3:
        if teamloaded == True:
            ChangeTeam(team)
        else:
            print("You need to load a team first")
    
    elif choice == 4:
        if teamloaded == True:
            SaveTeam(team)
        else:
            print("You need to load a team first")
    
    elif choice == 5:
        if teamloaded == True:
            choice2 = input("Would you like to save first? (Y/N)")
            if choice2.upper() == "Y":
                SaveTeam(team)
                break
        else:
            break

    else:
        print("Invalid input")

