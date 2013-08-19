def next():
	next = 0
	n = prime[len(prime)-1]
	print n
	while True:
		n+=1
		for a in prime:
			if a>=(n/2)+1:
				next = n
			if n%a==0:
				break
		if next==n:
			break
	return [next]


		


if __name__=="__main__":
	print 1
	prime = [2]
	while raw_input("another?")!='n':
		prime += next()