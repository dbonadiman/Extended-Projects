def squaresum_of_digits(n):
	summ = 0
	for a in str(n):
		summ += int(a)**2
	return summ

def happy_number(n):
	previous_number = [n]
	while n!=1:
		n = squaresum_of_digits(n)
		if n in previous_number:
			return False
		previous_number.append(n)
	return True 


def first_eight_hn():
	happy_numbers = []
	i=0
	while True:
		i+=1
		if happy_number(i):
			happy_numbers.append(i)
		if len(happy_numbers)==8:
			return happy_numbers



def main():
	try:
		n = int(raw_input("N: "))
	except Exception, e:
		print "Wrong Input,retry."
		main()
	else:
		if happy_number(n):
			print "{} is an Happy Number".format(n)
		else:
			print "{} is not an Happy Number".format(n)
		print "The first 8 happy numbers are {}".format(first_eight_hn())



if __name__=="__main__":
	main()