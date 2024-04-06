def GetHP(player, opponents):
    newopponents = []

    try:
        playerhp = int(input("What HP is your Pokemon currently at? "))
    except:
        print("Invalid input")
        return GetHP(player,opponents)
    
    #makes sure player HP does not exceed max hp
    if playerhp > player.gethp() or playerhp < 0:
        print("Invalid input")
        return GetHP(player,opponents)
    player.sethp(playerhp)


    try:
        enemyhp = float(input("What percentage of their HP does the opponent currently have? "))
    except:
        print("Invalid input")
        return GetHP(player,opponents)

    if enemyhp > 100 or enemyhp < 0:
        print("Invalid input")
        return GetHP(player,opponents)
    #calculates HP percentage for each opponent in list
    for i in opponents:
        temp = i.getcurrenthp()
        temp = int(temp)
        temp2 = round((temp * enemyhp)/100)
        if enemyhp != 0 and temp2 < 1:
            temp2 = 1
        i.setcurrenthp(temp2)
        newopponents.append(i)
    opponents = newopponents
    return (player,opponents)