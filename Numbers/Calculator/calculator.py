def operation(n1,n2,op):
    return {
        '+':n1+n2,
        '-':n1-n2,
        '*':n1*n2,
        '/':n1/n2
    }.get(op,"Wrong operator")

def main():
    try:
        n1 = int(input("Number 1: "))
        n2 = int(input("Number 2: "))
    except Exception:
        print("Wrong input, retry.")
        main()
    else:
        operator = str(input("Operator(+,-,*,/)"))
        print(operation(n1,n2,operator))

if __name__=="__main__":
    main()