"""
Problem
-------
**Mortgage Calculator**

Calculate the monthly payments of a fixed
term mortgage over given Nth terms at a given
interest rate. Also figure out how long it
will take the user to pay back the loan.


Solution
--------
A function to calculate the montly payments and
one to find the total amount to pay

Author
------
dbonadiman

"""
import sys


def total_mortgage(montly_amount, months):
    """
    Calculate the total amounts given
    the montly amount and the number of
    months

    >>> total_mortgage(1000,12)
    12000
    """
    return montly_amount*months


def montly_amount(mortgage, months, interest_rate):
    """
    Calculate the montly amount to pay given
    the mortgage amount, the annual interest rate
    and the number of months

    M*C*(1+C)^N
    -----------
    ((1+C)^N)-1

    >>> montly_amount(100,12,0.1)
    8.79
    """
    montly_interest = interest_rate/12
    num = ((mortgage*(montly_interest)*(1+montly_interest)**months))
    den = (((1+montly_interest)**months)-1)
    return round(num/den, 2)


def main():
    print("\nThis program calculate how much do you have to pay\n"
          "to pay back a Mortgage given the number of month and\n"
          "the interest rate\n")
    mortgage = float(raw_input("Mortgage amount? "))
    interest_rate = float(raw_input("Interest rate? "))
    terms = float(raw_input("Terms(in month) "))
    montly = montly_amount(mortgage, terms, interest_rate)
    print("Montly fee {:.2f}".format(montly))
    print("Total {:.2f} ".format(total_mortgage(montly, terms)))
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
