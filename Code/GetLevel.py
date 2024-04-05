def GetLevel():
	try:
		level = int(input("What level of the battle tower are you currently at? "))
		
	#validation to make sure input is greater than one and integer
	except:
		print ("Input must be integer")
		level = GetLevel()

	if level < 1:
		print ("Input must be greater than zero")
		level = GetLevel()

	return level