"""
Problem
-------
**Connected Graph**
Create a program which takes a graph
as an input and outputs whether every
node is connected or not.


Solution
--------
This is a self crafted solution to the
connected graph problem.

It can haves some error on special cases

Author
------
dbonadiman

"""
import sys
from copy import deepcopy


def strong_connectivity(graph, node):
    """
    strong_connectivity
    This function is based on the one for the eulerian path
    whith the difference that it returns True if the graph
    is connected False otherwise

    Parameter:

    graph ==> a list of list (matrix) that represent a graph

    node ==> the node to start

    Requirement:

    from copy import deepcopy

    Test:

    >>> strong_connectivity([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,1,0]],0)
    True

    >>> strong_connectivity([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]],0)
    True

    >>> strong_connectivity([],0)
    True
    """
    if graph in [[], [[1]], [[0]]]:
        return True
    else:
        return strong_connectivity_r(deepcopy(graph),
                                     [1]*len(graph),
                                     [node],
                                     sum(sum(x for x in i) for i in graph))


def strong_connectivity_r(visited, nodes, path, edges_left):
    """
    strong_connectivity_r
    This function takes in input a graph and a list of nodes with
    a path and the number of edges left and search for an eulerian
    path starting from this node.

    Parameter:

    visited ==> a list of list (matrix) that represent a graph
                with the node edges to visit setted at 1

    nodes ==> an array that represent the nodes the one at 1 are the
              ones not visited yet

    path ==> is the path to reach this node.

    edges_left ==> is a counter of the edges_left to visit
                   is kept in order to avoid an iteration over the
                   whole matrix when it's needed.

    Requirement:

    from copy import deepcopy

    Test:

    >>> graph = ([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
    >>> strong_connectivity_r(deepcopy(graph),[1] * 4,[0], 4)
    True
    """
    if len(path) > 1:
        visited[path[-2]][path[-1]] = 0
    nodes[path[-1]] = 0
    nodes_to_visit = sum(x for x in nodes)
    if not nodes_to_visit:
        return True
    for i in [0, 1]:
        for j in range(len(nodes)):
            if visited[path[-1]][j]:
                if not nodes[j] == i:
                    out = strong_connectivity_r(deepcopy(visited), nodes,
                                                deepcopy(path+[j]),
                                                edges_left-1)
                    if out:
                        return out
    return False


def connected(graph):
    """
    That's only a wrapper of strong connectiviy
    """
    return strong_connectivity(graph, 0)


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
        print("\nThis program takes in input some graphs and outputs\n"
              "True if the graph is connected False Otherwise\n")

        graph = [[0, 1, 0, 0],
                 [1, 0, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]]
        print_matrix(graph)
        print("\n Connected: {}\n".format(connected(graph)))
        graph = [[0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1],
                 [1, 0, 0, 0]]
        print_matrix(graph)
        print("\n Connected: {}\n".format(connected(graph)))
        graph = [[0, 1, 0, 1],
                 [0, 0, 1, 0],
                 [1, 0, 0, 0],
                 [0, 0, 0, 0]]
        print_matrix(graph)
        print("\n Connected: {}\n".format(connected(graph)))
        graph = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        print_matrix(graph)
        print("\n Connected: {}\n".format(connected(graph)))
        graph = [[1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1]]
        print_matrix(graph)
        print("\n Connected: {}\n".format(connected(graph)))
        graph = []
        print_matrix(graph)
        print("\n Connected: {}\n".format(connected(graph)))
        graph = [[1]]
        print_matrix(graph)
        print("\n Connected: {}\n".format(connected(graph)))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
