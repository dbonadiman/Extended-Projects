def pig_latin(s):
	return s[1:]+"-"+s[0]+"ay"

def main():
	try:
		string = raw_input("")
	except Exception, e:
		print "Wrong input,retry."
		main()
	else:
		print pig_latin(string)

if __name__=="__main__":
	main()
