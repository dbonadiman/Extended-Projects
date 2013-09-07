"""
Problem
-------
**Credit Card Validator**
Takes in a credit card number
from a common credit card vendor
(Visa, MasterCard, American Express, Discoverer) and
validates it to make sure that it is a valid number
(look into how credit cards use a checksum).


Solution
--------
Validate the credit card using the Luhn "Mod 10"
algorithm

https://en.wikipedia.org/wiki/Luhn_algorithm

Author
------
dbonadiman

"""
import sys


def is_valid(number):
    """
    This function checks if a credit card number
    is valid using the Mod-10 algorithm.

    >>> is_valid("479410028 3427946")
    True

    >>> is_valid("455629_5908122936")
    False

    >>> is_valid("4556295908122936")
    True

    """
    try:
        out = []
        revrs = number[::-1].replace(' ', '')
        for i, n in enumerate(revrs):
            if i % 2 == 0:
                out.append(int(n))
            else:
                times_n = str(int(n)*2)
                summ = sum(int(d) for d in times_n)
                out.append(summ)
        return sum(out) % 10 == 0
    except Exception, e:
        return False


def main():
    try:
        print("\nThis programm checks if the follows credit"
              " card numbers are valid\n")

        print("479410028 3427946 >> {}\n"
              "".format(is_valid("479410028 3427946")))
        print("4556295908122936 >> {}\n"
              "".format(is_valid("4556295908122936")))
        print("455629_5908122936 >> {}\n"
              "".format(is_valid("455629_5908122936")))
        print("60113335790095811 >> {}\n"
              "".format(is_valid("60113335790095811")))
        return 0
    except Exception, e:
        print(e)
        return 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
