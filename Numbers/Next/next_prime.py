"""
Problem
-------

**Next Prime Number**
Have the program find prime numbers until the user
chooses to stop asking for the next one.

Solution
--------
The problem is solved using an iterative and a recursive
 tecniques

Author
------
dbonadiman

"""
import sys


def next_recursive(n=0):
    """
    Prime Factorization in an recursive algorithm.

    >>> next_recursive(3)
    5

    >>> next_recursive(1)
    2

    >>> next_recursive()
    1
    """
    n += 1
    # Optimisation:
    # we try to divide only by 2 and the
    # odds number between 3 and the
    # candidate div 2
    div = range(3, int(n/2), 2)
    if n != 2:
        div.append(2)
    for a in div:
        if n % a == 0:
            return next_recursive(n)
    return n


def next_iterative(n=0):
    """
    Prime Factorization in an recursive algorithm.

    >>> next_iterative(3)
    5

    >>> next_iterative(1)
    2

    >>> next_iterative()
    1
    """
    while True:
        n += 1
        div = range(3, int(n/2), 2)
        if n != 2:
            div.append(2)
        divisible = False
        for a in div:
            divisible = divisible or (n % a == 0)
        if not divisible:
            break
    return n


def main():
    n_r = next_recursive()
    n_i = next_recursive()
    while not raw_input("Press enter to get another prime number! "
                        "(q to quit)").lower().startswith('q'):
        print("Recursive: {}".format(n_r))
        n_r = next_recursive(n_r)
        print("Iterative: {}".format(n_i))
        n_i = next_recursive(n_i)
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
