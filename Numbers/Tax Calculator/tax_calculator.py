import sys

def _setup():
    global input
    try: input = raw_input
    except NameError: pass

def main():
    tax_amount = float(input("Tax --> "))
    cost = float(input("Cost --> "))
    print("You will pay: {:.2f} ".format(tax_amount*cost+cost))

if __name__=="__main__":
    _setup()
    status = main()
    sys.exit(status)