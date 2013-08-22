def reverse(s):
	return s[::-1]

def main():
	try:
		string = raw_input("")
	except Exception, e:
		print "Wrong input, retry."
		main()
	else:
		print reverse(string)


if __name__=="__main__":
	main()