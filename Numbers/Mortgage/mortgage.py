def montly_amount(mortgage,months,interest_rate):
    return ((mortgage*(interest_rate/12)*(1+interest_rate/12)**months))/(((1+interest_rate/12)**months)-1)

def main():
    global input
    try: input = raw_input
    except NameError: pass
    INTEREST_RATE = 0.1
    TERMS  = 24
    mortgage = float(input("Mortgage amount?"))
    print("montly fee {}".format(montly_amount(mortgage,TERMS,INTEREST_RATE)))
    print("Total {} ".format(montly_amount(mortgage,TERMS,INTEREST_RATE)*TERMS))

if __name__=="__main__":
    main()