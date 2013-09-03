def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    return factorial

def factorial_rec(n):
    if n<=1:
        return 1
    else:
        return n*factorial_rec(n-1)

def main():
    try:
        n = int(input("N: "))
    except Exception:
        print ("Wrong input,retry.")
    else:
        print ("N! iterative : {}".format(factorial(n)))
        try:
            print ("N! recoursive : {}".format(factorial_rec(n)))
        except Exception:
            print("Too much recursion")
        
if __name__=="__main__":
    main()