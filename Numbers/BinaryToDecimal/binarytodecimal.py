def decimal_to_binary(num):
    binary = ""
    while num>0:
        binary+=str(num%2)
        num = int(num/2)
    return binary[::-1] #this reverse the string

def binary_to_decimal(bin):
    return sum((2)**((len(bin)-1)-i) if int(bin[i])==1 else 0 for i in range(len(bin)))

def main():
    try:
        global input
        try: input = raw_input
        except NameError: pass
        decimal = int(input("A decimal number: "))
        print (decimal_to_binary(decimal))
        binary = str(input("A binary number: "))
        print (binary_to_decimal(binary))
    except Exception:
        print("Wrong input,retry.")
        main()
    
if __name__=="__main__":
    main()