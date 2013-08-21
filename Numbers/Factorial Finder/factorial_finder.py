

def factorial(n):
	factorial = 1
	for i in range(1,n+1):
		factorial*=i
	return factorial

def factorial_rec(n):
	if n<=1:
		return 1
	else:
		return n*factorial_rec(n-1)

def main():
	try:
		n = int(raw_input("N: "))
	except Exception, e:
		print "Wrong input,retry."
	else:
		print "N! iterative : {}".format(factorial(n))
		print "N! recoursive : {}".format(factorial_rec(n))

if __name__=="__main__":
	main()