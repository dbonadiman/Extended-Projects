"""
Problem
-------
**Closest pair problem**
The closest pair of points problem
or closest pair problem is a problem
of computational geometry: given n
points in metric space, find a pair
of points with the smallest distance
between them.


Solution
--------

The solution is presented using
a brute force algorithm that runs in O(n^2)


Author
------
dbonadiman

"""
import sys
import math


def distance(a, b):
    """
    This is an implementation of the
    euclidean distance formula for the
    n dimensional space

    Parameter:
    a, b ==> two vector (tuple or list) that
             must have the same lenght

    Test:
    >>> distance((1, 2), (2, 1))
    1.4142135623730951

    >>> distance([3, 5, 7 ,8], [1, 2, 5, 6])
    4.58257569495584

    >>> distance([1], [2, 5])
    Traceback (most recent call last):
    ...
    AssertionError: Two different dimensional spaces
    """
    assert len(a) == len(b), "Two different dimensional spaces"

    return math.sqrt(sum((a[i]-b[i])**2 for i in range(len(a))))


def closest_pair(points):
    """
    This algorithm finds the closest pair of points
    in order to do that iterates over all the points
    and outputs the closest ones

    Complexity:
    O(n^2)

    Parameters:
    points ==> a list of points(vector in a geometric
               space)

    Test:

    >>> closest_pair([(1, 2, 4), (3, 2, 0), (1, 10, 1), (2, 1, 1)])
    ((3, 2, 0), (2, 1, 1))

    """
    minim = ((), float("inf"))
    for a in points:
        for b in points:
            if a is not b and distance(a, b) < minim[1]:
                minim = ((a, b), distance(a, b))
    return minim[0]


def main():
    try:
        print("\nThis program returns the closest pair of points"
              " given a list\n"
              "The following list is taken as example:\n")

        points = [(1, 2, 4), (3, 2, 0), (1, 10, 1), (2, 1, 1)]
        print(points)
        print(closest_pair(points))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
