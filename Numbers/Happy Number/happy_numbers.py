def squaresum_of_digits(n):
    return sum(int(a)*int(a) for a in str(n))

def happy_number(n):
    previous_number = [n]
    while n!=1:
        n = squaresum_of_digits(n)
        if n in previous_number:
            return False
        previous_number.append(n)
    return True 

def first_eight_hn():
    happy_numbers = []
    i=0
    while True:
        i+=1
        if happy_number(i):
            happy_numbers.append(i)
        if len(happy_numbers)==8:
            return happy_numbers

def main():
    try:
        n = int(input("N: "))
    except Exception:
        print("Wrong Input,retry.")
        main()
    else:
        if happy_number(n):
            print("{} is an Happy Number".format(n))
        else:
            print("{} is not an Happy Number".format(n))
        print("The first 8 happy numbers are {}".format(first_eight_hn()))

if __name__=="__main__":
    main()
