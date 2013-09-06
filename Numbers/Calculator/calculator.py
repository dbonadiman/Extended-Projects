"""
Problem
-------
**Calculator**
A simple calculator to do basic operators.
Make it a scientific calculator for added complexity.


Solution
--------
This program executes basic operation between float

Author
------
dbonadiman

"""
import sys


def operation(n1, n2, op):
    """
    Converts a binary string to a real number!

    >>> operation(3, 2, '+')
    5

    >>> operation(3, 2, '-')
    1

    >>> operation(3, 2, '*')
    6

    >>> operation(3.0, 2.0, '/')
    1.5

    >>> operation(3.0, 2.0, '^')
    Traceback (most recent call last):
        ...
    ValueError: Wrong operator only + - * / allowed

    """
    if op not in "+-*/":
        raise ValueError("Wrong operator only + - * / allowed")
    dic = {
        '+': n1+n2,
        '-': n1-n2,
        '*': n1*n2,
        '/': n1/n2
        }
    return dic.get(op)


def main():
    try:
        print("\nThis program converts decimal number to binary"
              "and vice-versa.\n")

        n1 = float(raw_input("Number 1: "))
        n2 = float(raw_input("Number 2: "))
        operator = str(raw_input("Operator (+, -, *, /): "))
        print("\n{} {} {} = {}".format(n1, operator,
                                       n2, operation(n1, n2, operator)))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
