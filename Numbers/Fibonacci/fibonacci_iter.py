def fibonacci():
	a=0
	b=1
	while n>b:
		print b
		c=b
		b=a+b
		a=c

def main():
	try:
		n = int(input("Give me a number:"))
	except Exception, e:
		print "Wrong input, retry."
		main()
	else:
		fibonacci()	
			
if __name__=="__main__":
	main()