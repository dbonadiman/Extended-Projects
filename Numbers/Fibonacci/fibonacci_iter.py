def fibonacci(n):
    a = 0
    b = 1
    while n>b:
        print(b)
        a,b = b,a+b

def main():
    try:
        global input
        try: input = raw_input
        except NameError: pass
        n = int(input("Give me a number:"))
    except Exception():
        print("Wrong input, retry.")
        main()
    else:
        fibonacci(n)    
            
if __name__=="__main__":
    main()