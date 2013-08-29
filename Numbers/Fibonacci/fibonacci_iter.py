def fibonacci(n):
	a=0
	b=1
	while n>b:
		print(b)
		c=b
		b=a+b
		a=c

def main():
	try:
		n = int(input("Give me a number:"))
	except Exception():
		print("Wrong input, retry.")
		main()
	else:
		fibonacci(n)	
			
if __name__=="__main__":
	main()