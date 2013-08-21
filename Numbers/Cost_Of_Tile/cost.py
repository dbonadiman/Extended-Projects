

class Square:
	def __init__(self,width,height):
		self.width = width
		self.height = height
	def __str__(self):
		return str(self.width)+"x"+str(self.height)


def input_float(string):
	try:
		return float(raw_input(string))
	except Exception, e:
		print "Wrong input, retry."
		return input_float(string)
	

def cost_of_tile(tile,floor, price):
	return (floor.width*floor.height*price)/(tile.width*tile.height)

def main():
	TILE = Square(0.5,0.5)
	price = input_float("What's the cost of a "+str(TILE)+" tile ($)? \n")
	width = input_float("What's the width of the floor? \n")
	height = input_float("What's the height of the floor? \n")
	floor = Square(width,height)
	print "The cost of tile is "+str(cost_of_tile(TILE,floor,price))+" $ \n"


if __name__=="__main__":
	main()
	


