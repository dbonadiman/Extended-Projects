"""
Problem
-------
**Dijkstras Algorithm**
Create a program that finds the shortest
path through a graph using its edges.


Solution
--------
The implementatipon of the dijkstra algorithm is
done representing the graph as a matrix.
It accepts, directed, undirected and weighted graphs

Author
------
dbonadiman

"""
import sys


def dijkstra(graph, source_node, destination):
    """
    dijkstra
    this algorithm takes in input a matrix representing
    the graph a source_node and a destination node
    and outputs the shortest path (the list of nodes in succession)
    through the graph using the dijkstra algorithm
    for the computation.

    Parameters:

    graph ==> a matrix representing the weighted graph
              in wich each node note represent the weight of
              the link

    source_node ==> the starting node

    destination ==> the destination node

    Test:
    >>> graph = [[0,2,1,0],[0,0,1,0],[0,3,0,1],[1,1,6,0]]
    >>> dijkstra(graph,1,0)
    [1, 2, 3, 0]

    >>> dijkstra(graph, 2, 0)
    [2, 3, 0]
    """
    if not graph:
        raise ValueError("Graph not Valid")
    nodes = set([i for i in range(len(graph))])
    dist = [0 if i is source_node else float("inf") for i in nodes]
    previous = [float("inf") for i in nodes]
    while nodes:
        val, idx = min((val, idx) for (idx, val) in enumerate(dist)
                       if idx in nodes)
        nodes.discard(idx)
        if val == float("inf"):
            break
        for (i, n) in enumerate(graph[idx]):
            if n > 0:
                a = val+graph[idx][i]
                if a < dist[i]:
                    dist[i] = a
                    previous[i] = idx
    sequence = []
    p = destination
    try:
        while True:
            sequence.append(p)
            p = previous[p]
            if p is source_node:
                break
        sequence.append(source_node)
    except Exception:
        return []
    return sequence[::-1]


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
        graph = [[0, 2, 1, 0],
                 [0, 0, 1, 0],
                 [0, 3, 0, 1],
                 [1, 1, 6, 0]]
        print_matrix(graph)
        for i in range(len(graph)):
            print("\nThe minimum path from {}"
                  " to {} are : {}\n".format(i, 0, dijkstra(graph, i, 0)))
        graph = []
        print_matrix(graph)
        try:
            print("\nThe minimum path from {}"
                  " to {} are : {}\n".format(0, 0, dijkstra(graph, 0, 0)))
        except ValueError:
            print("Graph not Valid")
        graph = [[0]]
        print_matrix(graph)
        try:
            print("\nThe minimum path from {}"
                  " to {} are : {}\n".format(0, 0, dijkstra(graph, 0, 0)))
        except ValueError:
            print("Graph not Valid")
        graph = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        print_matrix(graph)
        for i in range(len(graph)):
            print("\nThe minimum path from {}"
                  " to {} are : {}\n".format(i, 0, dijkstra(graph, i, 0)))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
