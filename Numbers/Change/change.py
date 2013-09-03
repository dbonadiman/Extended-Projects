EURO = [500.0,200.0,100.0,50.0,20.0,10.0,5.0,2.0,1.0,0.50,0.20,0.10,0.05,0.02,0.01]

def change(amount,coin):
    ret = {}
    for c in coin:        
        while c<=amount:
            ret[c] = ret.get(c, 0) + 1
            amount -= c
    return ret.items()

def main():
    try:
        global input
        try: input = raw_input
        except NameError: pass
        cost = float(input("Cost: "))
        money_given = float(input("Money given: "))
    except Exception:
        print("Wrong input, retry.")
        main()
    else:
        print ("The change is : {:.2f}".format(money_given-cost))
        for (coin,amount) in change(money_given-cost,EURO):
            print ("{} of {:.2f} euro".format(amount,coin))

if __name__=="__main__":
    main()