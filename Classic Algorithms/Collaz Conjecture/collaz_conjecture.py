

def collaz(num):
	steps = 0
	while True:
		if num==1:
			break
		steps += 1
		if num%2==0:
			num=int(num/2)
		else:
			num=num*3+1		
	return steps


def main():
	try:
		num = int(input("Number:"))
	except Exception:
		print("Wrong input, retry.")
		main()
	else:
		print(collaz(num))


if __name__ == "__main__":
	main()
