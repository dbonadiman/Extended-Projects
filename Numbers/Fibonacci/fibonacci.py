def fibonacci(n):
	fib(0,1,n)
	

def fib(a,b,n):
	if n>b:
		print b
		fib(b,a+b,n)
		
if __name__=="__main__":
	fibonacci(int(input("Give me a number:")))