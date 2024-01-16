from MainObject import *
def CreateTeam():
    team = []
    count = 0
    while count < 3:
        count +=1
        valid = False
        while valid == False:
            name = str(input("Enter the name of Pokemon number " + str(count) + " "))
            ##Do proper validation later
            if name != "Incorrect":
                valid = True
            if valid == False:
                print ("Invalid Pokemon species name (try checking spelling)")
        poke = Pokemon(name)
        ##Do type stuff later
        team.append(poke)
    return team