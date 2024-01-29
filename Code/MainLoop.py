from CreateTeam import *
from LoadTeam import *
from SaveTeam import *
from EditTeam import *

print("Welcome to the Pokemon battle tower helper")

teamloaded = False
recentlysaved = True

while True:
    try:
        choice = int(input("\nWhat would you like to do?\n1)Create a new team\n2)Load an existing team\n3)Edit the currently loaded team\n4)Save the currently loaded team\n5)Close the program\nPlease input the number:"))
    except:
        #just a filler line of code since code below already catches invalid values for choice
        choice = "Beans"

    #another big if statement, please learn to code
    if choice == 1:
        #check if team is not recently saved
        if recentlysaved == False:
            choice2 = input("Are you sure? This will erase the currently loaded team (Y/N)")
            if choice2.upper() == "Y":
                team = CreateTeam()
                teamloaded = True
                recentlysaved = True
        else:
            team = CreateTeam()
            teamloaded = True
            recentlysaved = True

    elif choice == 2:
        if recentlysaved == False:
            choice2 = input("Are you sure? This will erase the currently loaded team (Y/N)")
            if choice2.upper() == "Y":
                team = LoadTeam()
                teamloaded = True
                recentlysaved = True
        else:
            team = LoadTeam()
            teamloaded = True
            recentlysaved = True

    elif choice == 3:
        if teamloaded == True:
            ChangeTeam(team)
            recentlysaved = False
        else:
            print("You need to load a team first")
    
    elif choice == 4:
        if teamloaded == True:
            SaveTeam(team)
            recentlysaved = True
        else:
            print("You need to load a team first")
    
    elif choice == 5:
        if recentlysaved == False:
            #makes sure team isnt lost when forgetting to save
            choice2 = input("Would you like to save first? (Y/N)")
            if choice2.upper() == "Y":
                SaveTeam(team)
                break
            else:
                break
        else:
            break

    else:
        print("Invalid input")

