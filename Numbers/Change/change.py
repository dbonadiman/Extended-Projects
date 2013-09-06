"""
Problem
-------
**Change Return Program**

The user enters a cost and then the amount of money given.
The program will figure out the change and the number of
quarters, dimes, nickels, pennies needed for the change.


Solution
--------
Iterate over a list containing all the possible change.
Until the change is given!

Author
------
dbonadiman

"""
import sys


def change(amount):
    """
    Returns the change

    >>> change(100)
    [(100.0, 1)]

    >>> change(0)
    []

    >>> change(18.311)
    [(1.0, 1), (2.0, 1), (5.0, 1), (0.1, 1), (10.0, 1), (0.2, 1), (0.01, 1)]
    """
    euro = [500.0, 200.0, 100.0,
            50.0, 20.0, 10.0, 5.0,
            2.0, 1.0, 0.50, 0.20,
            0.10, 0.05, 0.02, 0.01]

    ret = {}
    for c in euro:
        while c <= amount:
            ret[c] = ret.get(c, 0) + 1
            amount -= c
    return ret.items()


def main():
    try:
        print("\nThis program returns the change given the cost"
              "and the money you give.\n")

        cost = float(raw_input("Cost: "))
        money_given = float(raw_input("Money given: "))
    except ValueError, e:
        print("\nOnly numbers allowed")
        return 1

    if cost < 0 or money_given < 0:
        print("\nOnly positive numbers allowed!")
        return 1

    if money_given-cost < 0:
        print("\nYou left to give {:.2f}$".format(abs(money_given-cost)))
    else:
        print ("\nThe change is : {:.2f}\n".format(money_given-cost))
        for (coin, amount) in change(money_given-cost):
            print ("{} of {:.2f} euro".format(amount, coin))
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
