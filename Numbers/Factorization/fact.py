def factorial(n):
	fact(n,2)

def fact(n,div):
	if find_div(n,div)==n:
		print n
	else:
		div = find_div(n,div)
		print div
		fact(n/find_div(n,div),div)
		

def find_div(n,div):
	a = div
	while n%a!=0:
		if a%2!=0:
			a +=1
		a +=1
	return a

if __name__=="__main__":
	factorial(int(input("Give me a number:")))