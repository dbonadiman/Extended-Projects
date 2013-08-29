###########################
# recursive one suffers of
# recursion limit exceeded on 
# large number.
##########################
def fibonacci(n):
	fib_rec(0,1,n)

def fib_rec(a,b,n):
	if n>b:
		print(b)
		fib_rec(b,a+b,n)
		
def main():
	try:
		n = int(input("Give me a number:"))
	except Exception:
		print ("Wrong input, retry.")
		main()
	else:
		fibonacci(n)	
			
if __name__=="__main__":
	main()