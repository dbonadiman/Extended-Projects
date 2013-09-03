####
# One is skipped
#####

def next(prime):
    next = 0
    n = prime[len(prime)-1]
    while True:
        n+=1
        for a in prime:
            if a>=(int(n/2))+1:
                next = n
            if n%a==0:
                break
        if next==n:
            return [next]

def main():
    print(2)
    prime = [2]
    while input()!='n':
        n = next(prime)
        print(n[0])
        prime += n
    
if __name__=="__main__":
    main()
