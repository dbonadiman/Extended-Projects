def fibonacci():
	a=0
	b=1
	while n>b:
		print b
		c=b
		b=a+b
		a=c

		
if __name__=="__main__":
	n = int(input("Give me a number:"))
	fibonacci()