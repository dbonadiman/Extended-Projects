__onetotwenty = {
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fiveteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen"
}

__dec = {
	20:"twenty",
	30:"thirty",
	40:"forty",
	50:"fifty",
	60:"sixty",
	70:"seventy",
	80:"eighty",
	90:"ninety"
}

__uptotrillion = {
	1000000000000:"trillion",
	1000000000:"billion",
	1000000:"million",
	1000:"thousand",
	100:"hundred"		
}

def digit_to_name(n):
	for dig in __uptotrillion.keys():
		if n/dig!=0:
			if n%dig == 0:
				return digit_to_name(n/dig)+" "+__uptotrillion[dig]
			else:
				return digit_to_name(n/dig)+" "+__uptotrillion[dig]+" "+digit_to_name(n%dig)

	if n<100 and n>=20:
		for dig in __dec.keys():
			if n-dig<10 and n-dig>0:
				return __dec[dig]+"-"+digit_to_name(n-dig)
			elif n-dig==0:
				return __dec[dig]

	return __onetotwenty[n]

def main():
	try:
		n = int(raw_input("N: "))
		if n==0:
			raise Exception('error','wrong input')
	except Exception, e:
		print "Wrong input, retry."
		main()
	else:
		print digit_to_name(n)


if __name__=="__main__":
	main()



