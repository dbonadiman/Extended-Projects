def words(s):
	return len([word for word in s.split(" ") if word not in ".,?!"] )

def main():
	try:
		text = raw_input("")
	except Exception, e:
		print "Wrong input,retry."
		main()
	else:
		print words(text)

if __name__=="__main__":
	main()