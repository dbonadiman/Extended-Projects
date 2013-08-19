if __name__=="__main__":
	DEF_wdt = 1.0
	DEF_heigh = 1.0
	price = float(raw_input("What's the cost of a "+str(DEF_wdt)+"x"+str(DEF_wdt)+" tile? "))
	wdt = float(raw_input("What's the width of the floor? "))
	height = float(raw_input("What's the height of the floor? "))
	print "The cost of tile is "+str((wdt*height*price)/(DEF_wdt*DEF_heigh))


