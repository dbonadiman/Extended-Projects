def sieve(n):
    if n%2==0: n+=1      
    temp = range(n,2,-2)
    prime = [2]
    while temp:
        prime.append(temp.pop())
        print(len(temp))
        for i,n in enumerate(temp):
            if n%prime[-1]==0:
                temp.pop(i)
    return prime 

def main():
    print sieve(1000000)

if __name__=="__main__":
    main()