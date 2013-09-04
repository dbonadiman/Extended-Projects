import sys

def montly_amount(mortgage,months,interest_rate):
    return ((mortgage*(interest_rate/12)*(1+interest_rate/12)**months))/(((1+interest_rate/12)**months)-1)

def main():
    global input
    try: input = raw_input
    except NameError: pass
    mortgage = float(input("Mortgage amount?"))
    interest_rate = float(input("Interest rate?"))
    terms  = float(input("Terms(in month)"))
    print("montly fee {:.2f}".format(montly_amount(mortgage,terms,interest_rate)))
    print("Total {:.2f} ".format(montly_amount(mortgage,terms,interest_rate)*terms))
    return 0

if __name__=="__main__":   
    sys.exit(main())