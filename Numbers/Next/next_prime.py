####
# One is skipped
#####

def next(prime):
    return next_p(prime[len(prime)-1]+1,prime)

def next_p(n,prime):
    for a in prime:
        if a>=(n/2)+1:
            return [n]
        if n%a==0:
            if n%2==0:
                return next_p(n+1)
            else:
                return next_p(n+2)
        
def main():
    print(2)
    prime = [2]
    while input()!='n':
        n = next(prime)
        print(n[0])
        prime += n

if __name__=="__main__":
    main()



        
