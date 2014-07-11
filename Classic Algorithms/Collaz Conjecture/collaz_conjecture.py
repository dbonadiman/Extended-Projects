"""
Problem
-------
**Collatz Conjecture**
Start with a number *n > 1*.
Find the number of steps it
takes to reach one using the
following process: If *n* is even,
divide it by 2. If *n* is odd,
multiply it by 3 and add 1.


Solution
--------
The implementatio is trivial.
It's only about follows the istruction
given by the problem description


Author
------
dbonadiman

"""
import sys


def collaz(num):
    """
    collaz

    This function calculates
    the number of steps needed
    to reach one.

    Parameters:
    num => the number, that must be
           greater than 0

    Test:
    >>> collaz(1)
    0

    >>> collaz(0)
    Traceback (most recent call last):
    ...
    AssertionError: The inserted number must be > 0

    >>> collaz(45)
    16
    """

    assert num > 0, "The inserted number must be > 0"

    steps = 0
    while not num == 1:
        steps += 1
        if not num % 2:
            num = int(num / 2)
        else:
            num = num*3+1
    return steps


def main():
    try:
        print("\nThis program allows you to test the collaz conjecture\n"
              "Passing as input a number the program returns"
              "the number of steps to reach 1 (because you always reach 1)\n"
              "Please enter the number:\n")

        num = int(raw_input("-->"))
        print("")
        print(collaz(num))
        return 0
    except Exception, e:
        print(e)
        return 1


def main2():
    i = 1
    while True:
        i += 1
        print(collaz(i))


if __name__ == "__main__":
    main()
