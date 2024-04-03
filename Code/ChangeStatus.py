def ChangeStatus(player, opponents):
    #1 burn
    #2 freeze
    #3 paralysis
    #4 poison
    #5 toxic
    #6 sleep
    #7 none
    playerstatus = input("What status condition does your Pokemon currently have?\n1)Burn\n2)Freeze\n3)Paralysis\n4)Poison\n5)Toxic\n6)Sleep\n7)None\nPlease input the number: ")
    try:
        playerstatus = int(playerstatus)
    except:
        print("Invalid input")
        return ChangeStatus(player,opponents)
    
    #sets status based on input
    if playerstatus == 1:
        player.setstatus("Burn")
    elif playerstatus == 2:
        player.setstatus("Freeze")
    elif playerstatus == 3:
        player.setstatus("Paralysis")
    elif playerstatus == 4:
        player.setstatus("Poison")
    elif playerstatus == 5:
        player.setstatus("Toxic")
    elif playerstatus == 6:
        player.setstatus("Sleep")
    elif playerstatus == 7:
        player.setstatus("None")
    else:
        print("Invalid input")
        return ChangeStatus(player,opponents)
    
    newopponents = []
    enemystatus = input("What status condition does the opponent Pokemon currently have?\n1)Burn\n2)Freeze\n3)Paralysis\n4)Poison\n5)Toxic\n6)Sleep\n7)None\nPlease input the number: ")
    try:
        enemystatus = int(enemystatus)
    except:
        print("Invalid input")
        return ChangeStatus(player,opponents)
    
    for i in opponents:
        if enemystatus == 1:
            i.setstatus("Burn")
        elif enemystatus == 2:
            i.setstatus("Freeze")
        elif enemystatus == 3:
            i.setstatus("Paralysis")
        elif enemystatus == 4:
            i.setstatus("Poison")
        elif enemystatus == 5:
            i.setstatus("Toxic")
        elif enemystatus == 6:
            i.setstatus("Sleep")
        elif enemystatus == 7:
            i.setstatus("None")
        else:
            print("Invalid input")
            return ChangeStatus(player,opponents)
        newopponents.append(i)
    opponents = newopponents
        
    return(player,opponents)
    

