def palindrome(s):
	for i in range(0,len(s)):
		if s[i]!=s[(len(s)-1)-i]:
			return False
	return True

def main():
	try:
		string = raw_input("")
	except Exception, e:
		print "Wrong input, retry."
		main()
	else:
		print palindrome(string)


if __name__=="__main__":
	main()