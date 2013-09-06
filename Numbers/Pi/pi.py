"""
Problem
-------

**Find PI to the Nth Digit**
Enter a number and have the program generate PI up to that
many decimal places. Keep a limit to how far the program
will go.

Solution
--------
I'm gonna use the default pi from the math module
formatting it using the string formatting function
(format).

Author
------
dbonadiman

"""
import math
import sys


def pi(precision):
    """
    Print Pi.

    >>> pi(3)
    '3.142'

    >>> pi(0)
    '3'

    >>> pi(50)
    '3.14159265358979311599796346854418516159057617187500'
    """
    outstring = ''.join(['{:.', str(precision), 'f}'])
    #TODO: find a more precise pi function then math.pi
    return outstring.format(math.pi)


def main():
    try:
        print("\nThis program returns the pi up to many"
              "decimal you enter.\n"
              "Please enter the number of decimal you need.\n")
        # the follow statement only works in 2.* change to input("-->") in 3.*
        precision = raw_input("-->")
        print(''.join(['\n', pi(int(precision)), '\n']))
        return 0
    except ValueError:
        print "Only positive integers allowed!\n"
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
