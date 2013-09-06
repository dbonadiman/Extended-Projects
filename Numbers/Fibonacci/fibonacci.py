"""
Problem
-------

**Fibonacci Sequence**

Enter a number and have the program generate the
Fibonacci sequence to that number or to the Nth number.

Solution
--------
The problem is solved using an iterative, a recursive and
a dynamic programming tecniques

Author
------
dbonadiman

"""
import sys


def fibonacci_dyprogramming(n):
    """
    Fibonacci in dynamic programming way.

    >>> fibonacci_dyprogramming(3)
    [0, 1, 1, 2, 3]

    >>> fibonacci_dyprogramming(0)
    [0]
    """
    fib_sequence = []
    if n > -1:
        fib_sequence.append(0)
    if n > 0:
        fib_sequence.append(1)
        while True:
            fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
            if fib_sequence[-1] > n:
                fib_sequence.pop()
                break
    return fib_sequence


def fibonacci_iterative(n):
    """
    Fibonacci in an iterative way.

    >>> fibonacci_iterative(3)
    [0, 1, 1, 2, 3]

    >>> fibonacci_iterative(0)
    [0]
    """
    a = 0
    b = 1
    fib_sequence = []
    while n >= a:
        fib_sequence.append(a)
        a, b = b, a+b  # i <3 python
    return fib_sequence


def fibonacci_recursive(n, a=0, b=1):
    """
    Fibonacci in an recursive algorithm.

    >>> fibonacci_recursive(3)
    [0, 1, 1, 2, 3]

    >>> fibonacci_recursive(0)
    [0]
    """
    if n >= a:
        return [a]+fibonacci_recursive(n, b, a+b)
    else:
        return []


def main():
    try:
        print("\nThis program returns the fibonacci sequence"
              "to a number you enter using two differents \n"
              "algorithms one iterative and one recursive.\n"
              "Please enter the number.\n")
        n = int(raw_input("--> "))
        if n < 0:
            raise ValueError()
    except ValueError:
        print("Only positive integers allowed!\n")
        return 1
    else:
        print("\n Recursive: {}".format(fibonacci_recursive(n)))
        print("\n Iterative: {}".format(fibonacci_iterative(n)))
        print("\n Dynamic Programming: {}".format(fibonacci_dyprogramming(n)))
        return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
