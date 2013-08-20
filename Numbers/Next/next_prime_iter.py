####
# One is skipped
#####

def next():
	next = 0
	n = prime[len(prime)-1]
	while True:
		n+=1
		for a in prime:
			if a>=(n/2)+1:
				next = n
			if n%a==0:
				break
		if next==n:
			return [next]

def main():
	print 2
	prime = [2]
	while raw_input()!='n':
		n = next()
		print n[0]
		prime += n
	
if __name__=="__main__":
	main()
