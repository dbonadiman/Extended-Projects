"""
Problem
-------
**Happy Numbers**

A happy number is defined by the following process.
Starting with any positive integer, replace the number
by the sum of the squares of its digits, and repeat
the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy
numbers, while those that do not end in 1 are unhappy numbers.
Display an example of your output here. Find first 8 happy
numbers.


Solution
--------
The solution is found using an iterative method
It allows to check if a specific number is an happy number
and obtains the list of the first 8 happy number


Author
------
dbonadiman

"""
import sys


def sqsum_of_digits(n):
    """
    sqsum_of_digits

    This function take in input a number
    and execute the summ of the square of each
    digit of the number

    Parameter:

    n ==> the number that can be either an integer
          or a string

    Test:

    >>> sqsum_of_digits(10)
    1

    >>> sqsum_of_digits('12')
    5

    >>> sqsum_of_digits(9)
    81

    >>> sqsum_of_digits(3.2)
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: '.'
    """
    return sum(int(a)*int(a) for a in str(n))


def happy_number(n):
    """
    happy number

    This algorithm iteratively execute the
    squere sum of the digit of a given
    number and stops when this squered
    sum of digit ends to 1 or the output
    is a number previously appeared in the
    iteration.
    In the first case the algorithm returns
    True; in the second case the algorithm returns
    False

    Parameter:

    n ==> this number has to be and integer

    Test:

    >>> happy_number(10)
    True

    >>> happy_number(2)
    False

    >>> happy_number(3.2)
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: '.'
    """
    previous_number = [n]
    while n != 1:
        n = sqsum_of_digits(n)
        if n in previous_number:
            return False
        previous_number.append(n)
    return True


def first_hn():
    """
    first_hn
    This function returns the first 8 happy numbers


    Test:
    >>> first_hn()
    [1, 7, 10, 13, 19, 23, 28, 31]
    """
    happy_numbers = []
    i = 0
    while True:
        i += 1
        if happy_number(i):
            happy_numbers.append(i)
        if len(happy_numbers) == 8:
            return happy_numbers


def main():
    try:
        print("\nThis program allows to check if a given number\n"
              "is an happy number and outputs the list of the first"
              " 8 happy numbers\n"
              "Please enter the number:\n")

        n = int(input("-->"))
        if happy_number(n):
            print("\n{} is an Happy Number\n".format(n))
        else:
            print("\n{} is not an Happy Number\n".format(n))
        print("The first 8 happy numbers are {}\n".format(first_hn()))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
