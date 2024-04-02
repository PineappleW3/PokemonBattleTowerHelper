def BonusInfo():
    #user inputs weather by selecting relevant input
    #1 = rain
    #2 = sun
    #3 = sand
    #4 = hail
    try:
        weather = int(input("What is the current weather condition?\n1)Rain\n2)Sun\n3)Sand\n4)Hail\nPlease input the number: "))
    except:
        print("Invalid input")
        return BonusInfo()
    if weather < 1 or weather > 4:
        print("Invalid input")
        return BonusInfo()
		
	
	
    reflect = input("Has the opponent used reflect?(Y/N) ")
    #converts input to boolean for future ease of use
    if reflect.title == "Y":
        reflect = True
    else:
        reflect = False

    screen = input("Has the opponent used light screen?(Y/N) ")
    if screen.title == "Y":
        screen = True
    else:
        screen = False

    wind = input("Has the opponent used tailwind?(Y/N) ")
    if wind.title == "Y":
        wind = True
    else:
        wind = False

    bonus =  [weather,reflect,screen,wind]
    return bonus