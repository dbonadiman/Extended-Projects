"""
Problem
-------
**Tax Calculator**
Asks the user to enter a cost
and either a country or state tax.
It then returns the tax plus
the total cost with tax.


Solution
--------
a simple function that calculates the
tax to pay


Author
------
dbonadiman

"""
import sys


def tax_calculator(tax, cost):
    """
    Tax_calculator
    07 Sep 2013

    This function is used to calculate tax
    plus the the total cost plus tax

    Parameter:

     tax => must be a float in the form 0.21 to
            represent a 21'%' tax

     cost => the cost of the goods to buy

    Test:

    >>> tax_calculator(0.1, 100)
    10.0

    >>> tax_calculator(0, 100)
    0.0

    >>> tax_calculator(1.0, 100)
    100.0
    """
    return float(tax * cost)


def main():
    try:
        print("\nThis program calculate amount you have to pay given\n"
              "the tax of your state and the cost of the good\n")

        print("Please enter the Tax to pay (0.21 not 21%)")
        tax = float(raw_input("--> "))
        print("Please enter the Cost of the good")
        cost = float(raw_input("--> "))

        print("You will pay: {:.2f} ".format(tax_calculator(tax, cost)+cost))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
