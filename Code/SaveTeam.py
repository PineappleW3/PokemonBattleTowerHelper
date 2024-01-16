def SaveTeam(team):
    filed = input("What would you like to name the file? ")
    if filed.find('.') == -1:
        filed = filed + ".txt"

    team1 = team[0]
    team2 = team[1]
    team3 = team[2]

    f = open(filed, "w")

    f.write(team1.getname())
    f.write(team1.getitem())
    f.write(team1.getability())
    f.write(team1.gethp())
    f.write(team1.getattack())
    f.write(team1.getdefense())
    f.write(team1.getspatk())
    f.write(team1.getspdef())
    f.write(team1.getspeed())
    f.write(team1.getmoves()[0])
    f.write(team1.getmoves()[1])
    f.write(team1.getmoves()[2])
    f.write(team1.getmoves()[3])

    f.write("$\n")

    f.write(team2.getname())
    f.write(team2.getitem())
    f.write(team2.getability())
    f.write(team2.gethp())
    f.write(team2.getattack())
    f.write(team2.getdefense())
    f.write(team2.getspatk())
    f.write(team2.getspdef())
    f.write(team2.getspeed())
    f.write(team2.getmoves()[0])
    f.write(team2.getmoves()[1])
    f.write(team2.getmoves()[2])
    f.write(team2.getmoves()[3])

    f.write("$\n")

    f.write(team3.getname())
    f.write(team3.getitem())
    f.write(team3.getability())
    f.write(team3.gethp())
    f.write(team3.getattack())
    f.write(team3.getdefense())
    f.write(team3.getspatk())
    f.write(team3.getspdef())
    f.write(team3.getspeed())
    f.write(team3.getmoves()[0])
    f.write(team3.getmoves()[1])
    f.write(team3.getmoves()[2])
    f.write(team3.getmoves()[3])

    
    f.close()
    return 5