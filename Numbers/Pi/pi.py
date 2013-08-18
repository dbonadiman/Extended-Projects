
###########################
# More precision is needed.
#
#
#
###########################
import sys

def pi():
	return 2*opi(1)

def opi(i):
	if i==50:
		return 1
	else:
		n = 1.0 + i / (2.0 * i + 1) * opi(i + 1)
		return n

if __name__=="__main__":
	print pi()