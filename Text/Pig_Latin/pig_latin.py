def pig_latin(s):
	return s[1:]+"-"+s[0]+"ay"

def main():
	try:
		string = input("")
	except Exception:
		print("Wrong input,retry.")
		main()
	else:
		print(pig_latin(string))

if __name__=="__main__":
	main()
