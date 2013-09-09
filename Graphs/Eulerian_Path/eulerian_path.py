"""
Problem
-------
**Eulerian Path**
Create a program which will take as an input
a graph and output either a Eulerian path or a
Eulerian cycle, or state that it is not possible.
A Eulerian Path starts at one node and traverses
every edge of a graph  through every node and finishes
at another node.  A Eulerian cycle is a eulerian
Path that starts and finishes at the same node.


Solution
--------
The solution is found in an recursive way
the function takes in input a matrix representing
the graph and outputs the corresponding Eulerian
Path / Cycle

Author
------
dbonadiman

"""
import sys
from copy import deepcopy


def eulerian_path(graph, node):
    """
    eulerian_path
    This function takes in input a graph and a node to start with
    and search for an eulerian path starting from this node.
    This function calls in particular sets up the input for a recursive
    function that execute the search for the Eulerian Path

    Parameter:

    graph ==> a list of list (matrix) that represent a graph

    node ==> the node to start

    Requirement:

    from copy import deepcopy

    Test:

    >>> eulerian_path([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,1,0]],0)

    >>> eulerian_path([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]],0)
    [0, 1, 2, 3, 0]

    >>> eulerian_path([],0)

    """
    if not graph:
        return None
    return eulerian_path_r(deepcopy(graph), [1]*len(graph),
                           [node], sum(sum(x for x in i) for i in graph))


def eulerian_path_r(visited, nodes, path, edges_left):
    """
    eulerian_path_r
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
    >>> eulerian_path_r(deepcopy(graph),[1] * 4,[0], 4)
    [0, 1, 2, 3, 0]

    """
    if len(path) > 1:
        visited[path[-2]][path[-1]] = 0
    nodes[path[-1]] = 0
    node_to_visit = sum(x for x in nodes)
    if not edges_left and not node_to_visit:
        return path
    for j, v in enumerate(nodes):
        if visited[path[-1]][j]:
            out = eulerian_path_r(deepcopy(visited),
                                  nodes, path+[j], edges_left-1)
            if out is not None:
                return out
    return None


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
              "the Eulerian paths for each of this graphs.\n"
              "If the path ends with the same node it starts the path is an\n"
              "Eulerian Cycle\n")

        graph = [[0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1],
                 [1, 0, 1, 0]]
        print_matrix(graph)
        print("\nPath: {}\n".format(eulerian_path(graph, 0)))
        graph = [[0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1],
                 [1, 0, 0, 0]]
        print_matrix(graph)
        print("\nPath: {}\n".format(eulerian_path(graph, 0)))
        graph = [[0, 1, 0, 1],
                 [0, 0, 1, 0],
                 [1, 0, 0, 0],
                 [0, 0, 0, 0]]
        print_matrix(graph)
        print("\nPath: {}\n".format(eulerian_path(graph, 0)))
        graph = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        print_matrix(graph)
        print("\nPath: {}\n".format(eulerian_path(graph, 0)))
        graph = [[1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1]]
        print_matrix(graph)
        print("\nPath: {}\n".format(eulerian_path(graph, 0)))
        graph = [[0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [1, 0, 0, 1],
                 [0, 0, 1, 0]]
        print_matrix(graph)
        print("\nPath: {}\n".format(eulerian_path(graph, 0)))
        graph = []
        print_matrix(graph)
        print("\nPath: {}\n".format(eulerian_path(graph, 0)))
        graph = [[1]]
        print_matrix(graph)
        print("\nPath: {}\n".format(eulerian_path(graph, 0)))
        graph = [[0]]
        print_matrix(graph)
        print("\nPath: {}\n".format(eulerian_path(graph, 0)))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
