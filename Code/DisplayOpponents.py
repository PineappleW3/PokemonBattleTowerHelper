def DisplayOpponents(opponents,expectedmoves):
    print("\n\n")
    counter = len(opponents)
    #loops for every potential opponent
    for i in range(0,counter):
        opponent = opponents[i]
        moves = expectedmoves[i]
        name = opponent.getname()
        print (name + " " + str(i+1))
        print("Held Item: " + opponent.getitem())
        print("Ability: " + opponent.getability())
        #shows every move
        moves2 = opponent.getmoves()
        for j in range(0,4):
            move2 = moves2[j]
            print("Move " + str(j+1) + ": " + move2)
            #strongest move from previous function
        print("Highest damage move: " + moves[0][0] + ", dealing " + str(moves[0][1]) + " damage")
        status = moves[1]
        print("Status moves:")
        for j in status:
            print (j)
        print("\n\n")

        