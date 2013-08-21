def factorial(n):
	div=2
	while True:
		div=find_div(n,div)
		print div
		if div!=n:
			n=n/div
		else:
			break
		

def find_div(n,div):
	a = div
	while n%a!=0:
		if a>n/2:
			return n 
		if a%2!=0:
			a +=1
		a +=1
	return a

def main():
	try:
		factorial(int(input("Give me a number:")))
	except Exception, e:
		print "Wrong input, retry."
		main()

if __name__=="__main__":
	main()
	