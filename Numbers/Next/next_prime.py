####
# One is skipped
#####

def next():
	return next_p(prime[len(prime)-1]+1)

def next_p(n):
	for a in prime:
		if a>=(n/2)+1:
			return [n]
		if n%a==0:
			if n%2==0:
				return next_p(n+1)
			else:
				return next_p(n+2)
		


if __name__=="__main__":
	print 2
	prime = [2]
	while raw_input()!='n':
		n = next()
		print n[0]
		prime += n


		
