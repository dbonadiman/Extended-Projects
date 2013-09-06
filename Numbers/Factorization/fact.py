"""
Problem
-------

**Prime Factorization**
Have the user enter a number and find all Prime Factors
(if there are any) and display them.

Solution
--------
The problem is solved using an iterative, a recursive
and dynamic programming tecniques

Author
------
dbonadiman

"""
import sys


def factorial_dyprogramming(n):
    """
    Prime Factorization in an dynamic programming algorithm.

    >>> factorial_dyprogramming(3)
    [3]

    >>> factorial_dyprogramming(35435)
    [5, 19, 373]

    >>> factorial_dyprogramming(0)
    []
    """
    prime_factors = []
    if n > 1:
        prime_factors.append(2)
        prime_factors.append(n)
        while True:
            prime_factors.insert(-1, _find_div(prime_factors[-1],
                                               prime_factors[-2]))
            if prime_factors[-2] == prime_factors[-1]:
                break
            prime_factors[-1] = int(prime_factors[-1]/prime_factors[-2])
    return prime_factors[1:-1]


def factorial_iterative(n):
    """
    Prime Factorization in an iterative algorithm.

    >>> factorial_iterative(3)
    [3]

    >>> factorial_iterative(35435)
    [5, 19, 373]

    >>> factorial_iterative(0)
    []
    """
    div = 2
    prime_factors = []
    while True and n > 1:
        div = _find_div(n, div)
        prime_factors.append(div)
        if div == n:
            break
        n = int(n/div)
    return prime_factors


def factorial_recursive(n, div=2):
    """
    Prime Factorization in an recursive algorithm.

    >>> factorial_recursive(3)
    [3]

    >>> factorial_recursive(35435)
    [5, 19, 373]

    >>> factorial_recursive(0)
    []
    """
    if n < 2:
        return []
    div = _find_div(n, div)
    if div == n:
        return [div]
    return [div]+factorial_recursive(int(n/div), div)


def _find_div(n, div=2):
    """
    This function finds a prime divisor of a given number
    starting from 2 or from a given divisor otherwise

    -- INTERNAL USAGE --
    """
    a = div
    while n % a != 0:
        if a > int(n/2):
            return n
        if a % 2 != 0:  # simple optimization
            a += 1
        a += 1
    return a


def main():
    try:
        print("\nThis finds all the prime prime factors of a"
              "given number \n"
              "Please enter the number.\n")
        n = int(raw_input("--> "))
        if n < 0:
            raise ValueError()
    except ValueError:
        print("Only positive integers allowed!\n")
        return 1
    else:
        print("\n Recursive: {}".format(factorial_recursive(n)))
        print("\n Iterative: {}".format(factorial_iterative(n)))
        print("\n Dynamic Programming: {}".format(factorial_dyprogramming(n)))
        return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
