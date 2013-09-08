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
found

Author
------
dbonadiman

"""
import sys
import time


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
    def primen(n):
        num = 5
        w = [2,4]
        nn = len(w)
        i = 0
        while num<=n:
           yield num
           num += w[i]
           i = (i+1)%nn

    start = time.time()       
    if n < 3:
        return []
    temp = [1]*n
    temp[0]=temp[1] = 0
    prime = [1, 2, 3]
    hop = 1
    for i in primen(n):
        if temp[i]:
            prime.append(i)
            if hop:
                t = time.time()
                hop=0
                for j in range(i*i,n,i):
                    # remove the number multiple than prime[-1]
                    if not j % i:
                        hop += 1
                        temp[j] = 0
    return prime 
    

def main():
    try:
        print(sieve(100000000))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
