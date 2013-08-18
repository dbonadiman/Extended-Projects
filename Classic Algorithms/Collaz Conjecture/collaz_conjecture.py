
import sys

def collaz(num):
	steps = 0
	while True:
		steps += 1
		if num%2==0:
			num=num/2
		else:
			num=num*3+1
		if num==1:
			break
	return steps




if __name__ == "__main__":
	num = int(sys.argv[1])
	if num>1:
		print collaz(num)
	else:
		print 'already one'  