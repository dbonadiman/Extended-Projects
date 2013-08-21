
def operation(n1,n2,op):
	return {
		'+':n1+n2,
		'-':n1-n2,
		'*':n1*n2,
		'/':n1/n2
	}[op]




def main():
	try:
		n1 = int(raw_input("Number 1: "))
		n2 = int(raw_input("Number 2: "))
	except Exception, e:
		print "Wrong input, retry."
		main()
	else:
		operator = raw_input("Operator(+,-,*,/)")
		print operation(n1,n2,operator) 

if __name__=="__main__":
	main()