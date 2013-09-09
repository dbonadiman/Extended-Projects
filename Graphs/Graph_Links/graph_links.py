"""
Problem
-------
**Graph from links**
Create a program that will create a graph or
network from a series of links.


Solution
--------
The solution is provided building a
matrix of 0 and 1 assigning 1 to the
field that represent a link.
More pratically for a link (1,2)
the node matrix[1][2] is assigned to 1

Author
------
dbonadiman

"""
import sys


def graph(links):
    """
    graph

    This function takes in input a list of links
    that are tuples and outputs a matrix that represent
    the graph created linking such node

    Note: The nodes names are allways between 0 and the
          maximum node label in the links list

    Parameters:

    links ==> a list of link, a link must be represented as
              a tuple (a, b) such that a is the starting node
              and b is the ending one

    Test:

    >>> graph([(1, 2), (0, 2)])
    [[0, 0, 1], [0, 0, 1], [0, 0, 0]]


    """
    m = max(max(n for (n, k) in links), max(k for (n, k) in links))
    graph = [[0]*(m+1) for i in range(m+1)]
    for (n, k) in links:
        graph[n][k] = 1
    return graph


def print_matrix(m):
    """
    print_matrix

    This is an ausiliary function that
    prints matrix in a more clear way
    and not as list of list

    Parameters:
    m ==> the matrix to print

    Test:
    >>> print_matrix([[0, 0, 1], [0, 0, 1], [0, 0, 0]])
    [0, 0, 1]
    [0, 0, 1]
    [0, 0, 0]
    """
    for l in m:
        print(l)


def main():
    try:
        print("\nThis program takes in input a list of links in a graph\n"
              "and gives as output the matrix representing the graph \n")

        links = [(1, 2), (2, 3)]
        print(links)
        print("")
        print_matrix(graph(links))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
