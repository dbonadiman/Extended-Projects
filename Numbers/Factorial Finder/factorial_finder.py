def factorial(n):
    factorial = 1
    for i in range(n):
        factorial*=i+1
    return factorial

def factorial_rec(n):
        return n*factorial_rec(n-1) if n>1 else 1

def main():
    try:
        global input
        try: input = raw_input
        except NameError: pass
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