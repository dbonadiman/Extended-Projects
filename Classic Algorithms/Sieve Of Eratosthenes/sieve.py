"""
Problem
-------
**Sieve of Eratosthenes**
The sieve of Eratosthenes is one of
the most efficient ways to find all
of the smaller primes (below 10 million
or so).


Solution
--------
The sieve is implemented using a list containing all
and the number between 2 and n (the number inserted)
and iteratively removing all the multiple of each prime
found.

The running time of that process on the interval
0 - 100.000.000 it's 40s finding 5761456 prime
numbers.

The running time for the first 1.000.000 is 0.49s
on a Mac Book Pro Mid 2009

Author
------
dbonadiman

"""
import sys


def sieve(n):
    """
    sieve

    The algotithm implements
    the Sieve of Eratosthenes in a fast and optimized way

    Parameters:
    n ==> n - 1 is the intervall in which the algorithm search
          for the prime numer

    Test:
    >>> sieve(10)
    [1, 2, 3, 5, 7]

    >>> sieve(0)
    []

    >>> sieve(20)
    [1, 2, 3, 5, 7, 11, 13, 17, 19]
    """
    def primen(a, n, l):
        """
        primen

        this inner-function is a generator
        that produces a sequence of number
        starting from 5 to n
        avoinding all the multiple of 2 and
        3 this speeds up a lot the sieve
        having a lot less number to process.

        >>> list(primen(5, 20, 1))
        [5, 7, 11, 13, 17, 19]
        """
        num = a
        w = [2, 4]
        nn = len(w)
        i = 0
        while num <= n:
            yield num
            num += w[i]*l
            i = (i+1) % nn

    if n < 3:
        return []
    temp = [1]*n
    temp[0] = temp[1] = 0
    prime = [1, 2, 3]
    hop = 1
    for i in primen(5, n, 1):
        if temp[i]:
            prime.append(i)
            if hop:
                hop = 0
                for j in range(i*i, n, i*2):
                    if not j % i:
                        hop += 1
                        temp[j] = 0
    return prime


def main():
    try:
        print("\nThis program execute the sieve of Eratosthenes\n"
              "between 0 and 10000000 and outputs the number of\n"
              "prime numbers found, please be patient it will\n"
              "took some time\n")

        #here we print only the lenght of the list
        #for visual constraint
        print("The nuber of prime numbers"
              " under 10000000 is {}".format(len(sieve(10000000))))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
