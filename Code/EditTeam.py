from MainObject import *
import sqlite3

#sets the directory for the database file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Pokemon.db')

connection = sqlite3.connect(filename)
cursor = connection.cursor()


def ChangeTeam(team):
    print("\nThese are your current team members:")
    count = 1
    for i in team:
        #shows a numbered list of every team member
        print(str(count) + ") " + i.getname())
        count+=1
    #select team member
    try:
        changer = int(input("Which one would you like to modify? Please input the number: "))
    except:
        print("Invalid input")
        team = ChangeTeam(team)
        return team
    if changer<1 or changer>3:
        print("Invalid input")
        team = ChangeTeam(team)
        return team
    #choose team member from array
    team[changer-1] = ChangeMember(team[changer-1])
    return team

def ChangeMember(teammember):
    #shows all information on current team member
    print ("\nThis is your current Pokemon")
    print ("Species = " + teammember.getname())
    print ("Item = " + teammember.getitem())
    print ("Ability = " + teammember.getability())
    print ("HP = " + str(teammember.gethp()))
    print ("Attack = " + str(teammember.getattack()))
    print ("Defense = " + str(teammember.getdefense()))
    print ("Special Attack = " + str(teammember.getspatk()))
    print ("Special Defense = " + str(teammember.getspdef()))
    print ("Speed = " + str(teammember.getspeed()))
    print ("Move 1 = " + teammember.getmoves()[0])
    print ("Move 2 = " + teammember.getmoves()[1])
    print ("Move 3 = " + teammember.getmoves()[2])
    print ("Move 4 = " + teammember.getmoves()[3])
    print("\n")
    
    
    try:
        change = int(input("What aspect would you like to change? \n1)Species \n2)Held Item \n3)Ability \n4)Stats \n5)Moves \nPlease input the number:"))
    except:
        print("Invalid input. Cancelling operation.")
        return teammember
    
    #big if statement to check output
    if change == 1:
        #check to avoid erasing data (in case of incorrect input or similar)
        check = input("Changing the Pokemon species will reset all other information about the Pokemon. Are you sure you want to change it? (Y/N)")
        if check.lower() == "y":
            teammember = ChangeSpecies(teammember)

    elif change == 2:
        teammember = ChangeItem(teammember)

    elif change == 3:
        teammember = ChangeAbility(teammember)

    elif change == 4:
        teammember = ChangeStats(teammember)

    elif change == 5:
        teammember = ChangeMoves(teammember)

    else:
        print("Invalid input. Cancelling operation.")
    return teammember
    
def ChangeSpecies(teammember):
    new = input("\nWhat Pokemon would you like to change to? ")
    new = new.title()
    #very similar code to CreateTeam
    rows1 = cursor.execute(
        "SELECT Type1, Type2 FROM PokemonSpecies WHERE Name = ?",
        (new,),
    ).fetchall()
    if len(rows1) > 0:
        rows1 = rows1[0]
        teammember = Pokemon(new)
        teammember.settype1(rows1[0])
        teammember.settype2(rows1[1])
    else:
        print("Invalid Pokemon species. Cancelling change.")
    return teammember

def ChangeItem(teammember):
    item = input("\nWhat would you like to change the item to? ")
    ##Add validation to item once item table is made
    teammember.setitem(item)
    return teammember

def ChangeAbility(teammember):
    abilitychoices = cursor.execute(
        "SELECT Abilities FROM PokemonSpecies WHERE Name = ?",
        (teammember.getname(),),
    ).fetchall()[0][0] #had to use the double index because returned value was within 2 lists
    abilitychoices = abilitychoices.split(",")
    print("\nThese are the abilities you can have:")
    
    #removes duplicate abilities from the list (looks better)
    ability2 = []
    for i in abilitychoices:
        if i in ability2:
            filler = 1
        else:
            ability2.append(i)
    abilitychoices = ability2

    count = 1
    #print numbered list of abilities
    for i in abilitychoices:
        print(str(count) + ") " + i)
        count+=1
    choice = input("Which ability would you like to choose? ")
    #validation to check ability is in list
    choice = choice.title()
    if choice in abilitychoices:
        teammember.setability(choice)
    else:
        print("Invalid ability. Cancelling change.")
    return teammember

def ChangeStats(teammember):
    try:
        choice = int(input("\nWhat stat would you like to change?\n1)HP\n2)Attack\n3)Defense\n4)Special Attack\n5)Special Defense\n6)Speed\n7)Finish changes\nPlease input a number: "))
    except:
        print("Invalid input. Finishing changes.")
        return teammember
    

    #big if statement to choose stat
    if choice == 1:
        basestat = cursor.execute(
            "SELECT Hp FROM PokemonSpecies WHERE Name = ?",
            (teammember.getname(),),
        ).fetchall()[0][0] #again needed because of output format

        #calculate upper and lower bounds for stat for validation use
        hpmin = ((2*basestat*50)/100)+60
        hpmax = ((((2*basestat)+94)*50)/100)+60
        valid = False
        #loop until valid input
        while valid == False:
            valid = True
            try:
                newstat = int(input("What would you like to change the Hp stat to? "))
                if newstat < hpmin or newstat > hpmax:
                    print("Input out of range. Try again")
                    valid = False
            except:
                print("Invalid input. Try again")
                valid = False
        teammember.sethp(newstat)

    #same validation on all of them
    elif choice == 2:
        basestat = cursor.execute(
            "SELECT Attack FROM PokemonSpecies WHERE Name = ?",
            (teammember.getname(),),
        ).fetchall()[0][0]
        statmin = (((((2*basestat))*50)/100)+5)*0.9
        statmax = (((((2*basestat)+94)*50)/100)+5)*1.1
        valid = False
        while valid == False:
            valid = True
            try:
                newstat = int(input("What would you like to change the Attack stat to? "))
                if newstat < statmin or newstat > statmax:
                    print("Input out of range. Try again")
                    valid = False
            except:
                print("Invalid input. Try again")
                valid = False
        teammember.setattack(newstat)

    elif choice == 3:
        basestat = cursor.execute(
            "SELECT Defense FROM PokemonSpecies WHERE Name = ?",
            (teammember.getname(),),
        ).fetchall()[0][0]
        statmin = (((((2*basestat))*50)/100)+5)*0.9
        statmax = (((((2*basestat)+94)*50)/100)+5)*1.1
        valid = False
        while valid == False:
            valid = True
            try:
                newstat = int(input("What would you like to change the Defense stat to? "))
                if newstat < statmin or newstat > statmax:
                    print("Input out of range. Try again")
                    valid = False
            except:
                print("Invalid input. Try again")
                valid = False
        teammember.setdefense(newstat)

    elif choice == 4:
        basestat = cursor.execute(
            "SELECT SpAtk FROM PokemonSpecies WHERE Name = ?",
            (teammember.getname(),),
        ).fetchall()[0][0]
        statmin = (((((2*basestat))*50)/100)+5)*0.9
        statmax = (((((2*basestat)+94)*50)/100)+5)*1.1
        valid = False
        while valid == False:
            valid = True
            try:
                newstat = int(input("What would you like to change the Special Attack stat to? "))
                if newstat < statmin or newstat > statmax:
                    print("Input out of range. Try again")
                    valid = False
            except:
                print("Invalid input. Try again")
                valid = False
        teammember.setspatk(newstat)

    elif choice == 5:
        basestat = cursor.execute(
            "SELECT SpDef FROM PokemonSpecies WHERE Name = ?",
            (teammember.getname(),),
        ).fetchall()[0][0]
        statmin = (((((2*basestat))*50)/100)+5)*0.9
        statmax = (((((2*basestat)+94)*50)/100)+5)*1.1
        valid = False
        while valid == False:
            valid = True
            try:
                newstat = int(input("What would you like to change the Special Defense stat to? "))
                if newstat < statmin or newstat > statmax:
                    print("Input out of range. Try again")
                    valid = False
            except:
                print("Invalid input. Try again")
                valid = False
        teammember.setspdef(newstat)

    elif choice == 6:
        basestat = cursor.execute(
            "SELECT Speed FROM PokemonSpecies WHERE Name = ?",
            (teammember.getname(),),
        ).fetchall()[0][0]
        statmin = (((((2*basestat))*50)/100)+5)*0.9
        statmax = (((((2*basestat)+94)*50)/100)+5)*1.1
        valid = False
        while valid == False:
            valid = True
            try:
                newstat = int(input("What would you like to change the Speed stat to? "))
                if newstat < statmin or newstat > statmax:
                    print("Input out of range. Try again")
                    valid = False
            except:
                print("Invalid input. Try again")
                valid = False
        teammember.setspeed(newstat)

    elif choice == 7:
        print("Finishing changes")
        return teammember
    else:
        print("Invalid input. Finishing changes.")
        return teammember
    #option to loop (woudld be miserable otherwise)
    choose2 = input("Would you like to make more changes to the stats? Y/N ")
    if choose2.upper() == "Y":
        teammember = ChangeStats(teammember)
    return teammember

def ChangeMoves(teammember):
    movelist = cursor.execute(
        "SELECT Moveset FROM PokemonSpecies WHERE Name = ?",
        (teammember.getname(),),
    ).fetchall()[0][0]
    movelist = movelist.split(",")
    #the database sometimes has whitespace on the last item for some reason
    movelist[len(movelist)-1] = movelist[len(movelist)-1].strip()
    currentmoves = teammember.getmoves()
    try:
        choice = int(input("\nWhich move slot would you like to change? "))
    except:
        print("Invalid input. Cancelling change")
        return teammember
    if choice<1 or choice>4:
        print("Invalid input. Cancelling change")
        return teammember
    
    newmove = input("What would you like to change the move to? ")
    #validate selection
    
    newmove = newmove.title()
    if newmove == "U-Turn":
        newmove = "U-turn"

    if newmove in movelist:
        currentmoves[choice-1] = newmove
        teammember.setmoves(currentmoves)
        return teammember
    else:
        print("Invalid move choice. Cancelling change")
        return teammember