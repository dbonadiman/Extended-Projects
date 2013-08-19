###########################
# recursive one suffers of
# recursion limit exceeded on 
# large number.
##########################
def fibonacci():
	fib()
	

def fib():
	a=0
	b=1
	while n>b:
		print b
		c=b
		b=a+b
		a=c



def fib_rec(a,b):
	if n>b:
		print b
		fib(b,a+b)
		
if __name__=="__main__":
	n = int(input("Give me a number:"))
	fibonacci()