def vowels(s):
	i = lambda s: i(s[1:])+1 if len(s)>0 and s[0] in "aeiou" else i(s[1:]) if len(s)>0 else 0
	return i(s)

def main():
	try:
		string = raw_input("")
	except Exception, e:
		print "Wrong input,retry."
		main()
	else:
		print vowels(string)


if __name__=="__main__":
	main()