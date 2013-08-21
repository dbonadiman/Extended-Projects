def decimal_to_binary(num):
	binary = ""
	while num>0:
		binary+=str(num%2)
		num = num/2
	return binary[::-1] #this reverse the string


def binary_to_decimal(bin):
	decimal = 0
	for i in range(0,len(bin)):
		if int(bin[i])==1:
			decimal += (2)**((len(bin)-1)-i)
	return decimal


def main():
	try:
		decimal = int(raw_input("A decimal number: "))
		print decimal_to_binary(decimal)
		binary = str(raw_input("A binary number: "))
		print binary_to_decimal(binary)
	except Exception, e:
		print "Wrong input, retry."
		main()



if __name__=="__main__":
	main()