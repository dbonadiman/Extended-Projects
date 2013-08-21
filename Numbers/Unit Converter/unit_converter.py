


__temp = {
	'C_K': lambda c: c+273.15,
	'K_C': lambda k: k-273.15,
	'C_F': lambda c: c*9.0/5.0+32.0,
	'F_C': lambda f: (f-32.0)*5.0/9.0,
	'F_K': lambda f: ((f-32.0)*5.0/9.0)+273.15,
	'K_F': lambda k: ((k-273.15)*9.0/5.0)+32.0
}


def main():
	try:
		f = raw_input("From (C,K,F): ")
		t = raw_input("To (C,K,F): ")
		a = float(raw_input("Amount: "))
	except Exception, e:
		print "Wrong input,retry."
		main()
	else:
		print __temp[f+"_"+t](a)


if __name__=="__main__":
	main()
