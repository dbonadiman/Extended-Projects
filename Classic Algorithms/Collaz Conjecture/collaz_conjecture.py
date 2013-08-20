
import sys

def collaz(num):
	steps = 0
	while True:
		if num==1:
			break
		steps += 1
		if num%2==0:
			num=num/2
		else:
			num=num*3+1		
	return steps


def main(argv):
	num = int(argv[1])
	print collaz(num) 


if __name__ == "__main__":
	main(sys.argv)
