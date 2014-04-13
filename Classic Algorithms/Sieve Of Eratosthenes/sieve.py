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
from array import array


def sieve(n):
    """
    sieve

    The algotithm implements
    the Sieve of Eratosthenes in a fast and optimized way

    Parameters:
    n ==> n - 1 is the intervall in which the algorithm search
          for the prime numer
    """
    def primen(a, n):
        """
        primen

        this inner-function is a generator
        that produces a sequence of number
        starting from 5 to n
        avoinding all the multiple of 2 and
        3 this speeds up a lot the sieve
        having a lot less number to process.
        """
        num = a
        w = [2, 4]
        i = 0
        while num <= n:
            yield num
            num += w[i]
            i = (i+1) % 2

    if n > 3:
        temp = array('H', [1])*n
        temp[0] = temp[1] = 0
        for i in range(1, 4):
            yield i
        hop = 1
        for i in primen(5, n):
            if temp[i]:
                if hop:
                    hop = 0
                    for j in range(i*i, n, i*2):
                        if not j % i:
                            hop = 1
                            temp[j] = 0
                yield i


def main():
    try:
        #here we print only the lenght of the list
        #for visual constraint
        print("The nuber of prime numbers"
              " under 10000000 is {}".format(len(list(sieve(10000000)))))
        return 0
    except Exception:
        return 1


if __name__ == "__main__":
    status = main()
    sys.exit(status)
