def GetHP(player, opponents):
    newopponents = []
    try:
        playerhp = int(input("What HP is your Pokemon currently at? "))
    except:
        print("Invalid input")
        return GetHP(player,opponents)
    if playerhp > player.gethp() or playerhp < 0:
        print("Invalid input")
        return GetHP(player,opponents)
    player.sethp(playerhp)


    try:
        enemyhp = float(input("What percentage of their HP does the opponent currently have? "))
    except:
        print("Invalid input")
        return GetHP(player,opponents)
    if enemyhp > 100 or playerhp < 0:
        print("Invalid input")
        return GetHP(player,opponents)
    for i in opponents:
        temp = i.getcurrenthp()
        if temp == "Max":
            temp = i.gethp()
        temp = int(temp)
        temp2 = round(temp * enemyhp)
        if enemyhp != 0 and temp2 < 1:
            temp2 = 1
        i.setcurrenthp(temp2)
        newopponents.append(i)
    opponents = newopponents
    return (player,opponents)
    

