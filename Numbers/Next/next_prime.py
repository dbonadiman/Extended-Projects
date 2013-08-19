def next():
	next = next_p(prime[len(prime)-1])
	print next
	return [next]

def next_p(n):
	n+=1
	for a in prime:
		if a>=(n/2)+1:
			return n
		if n%a==0:
			return next_p(n)
		


if __name__=="__main__":
	print 1
	prime = [2]
	while raw_input("another?")!='n':
		prime += next()


		
