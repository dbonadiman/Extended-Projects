"""
Problem
-------
**Factorial Finder**
The Factorial of a positive integer,
n, is defined as the product of the sequence
n, n-1, n-2, ...1 and the factorial of zero,
0, is defined as being 1. Solve this using
both loops and recursion.


Solution
--------
A solution is presented in both iterative and
recursive way :)


Author
------
dbonadiman

"""
import sys


def factorial_iterative(n):
    """
    factorial_iterative(n)

    This function computes the factorial
    of a number n in an iterative way

    Parameters:

    n ==> the integer used for to compute N!

    Tests:

    >>> factorial_iterative(5)
    120

    >>> factorial_iterative(0)
    1

    """
    factorial = 1
    for i in range(n):
        factorial *= i+1
    return factorial


def factorial_recursive(n):
    """
    factorial_recursive(n)

    This function computes the factorial
    of a number n in an recursive way

    Parameters:

    n ==> the integer used for to compute N!

    Tests:

    >>> factorial_recursive(5)
    120

    >>> factorial_recursive(0)
    1

    """
    return n * factorial_recursive(n-1) if n else 1


def main():
    try:
        n = int(raw_input("-->"))
        print ("N! iterative : {}".format(factorial_iterative(n)))
        print ("N! recoursive : {}".format(factorial_recursive(n)))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
