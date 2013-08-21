from collections import defaultdict 

EURO = [500.0,200.0,100.0,50.0,20.0,10.0,5.0,2.0,1.0,0.50,0.20,0.10,0.05,0.02,0.01]

def change(amount,coin):
	ret = defaultdict(int)
	for c in coin:
		while c<amount:
			ret[c] += 1
			amount -= c
	return ret.items()


def main():
	cost = float(input("Cost: "))
	money_given = float(input("Money given: "))
	print "The change is: "+str(money_given-cost)
	for (coin,amount) in change(money_given-cost,EURO):
		print str(amount)+" of "+str(coin)+" euro"



if __name__=="__main__":
	main()