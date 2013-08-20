def montly_amounts(mortgage,months,interest_rate):
	for i in range(1,months):
		print amount(mortgage/months,i,interest_rate)


def amount(cost, time, interest_rate):
	return cost*(1+time*interest_rate)



def main():
	INTEREST_RATE = 10.0
	TERMS  = 24
	mortgage = float(raw_input("Mortgage amount?"))
	montly_amounts(mortgage,TERMS,INTEREST_RATE)


if __name__=="__main__":
	main()