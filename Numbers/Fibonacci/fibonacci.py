###########################
# recursive one suffers of
# recursion limit exceeded on 
# large number.
##########################
def fibonacci():
	fib_rec(0,1)

def fib_rec(a,b):
	if n>b:
		print b
		fib_rec(b,a+b)
		
if __name__=="__main__":
	n = int(input("Give me a number:"))
	fibonacci()