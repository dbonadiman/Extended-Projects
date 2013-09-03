class Graph:
    _nodes = []
    _edges = []

    def __init__(self,nodes=None,edges=None):
        if nodes is not None:
            self.add_nodes(nodes)
        if edges is not None:
            self.add_edges(edges)

    def add_node(self, n):
        if n not in self.__nodes:
            self._nodes.append(n)

    def add_edge(self, a):
        if isinstance(a,tuple):
            if (a[0] in self._nodes) and (a[1] in self.__nodes):
                if a not in self._edges:
                    self._edges.append(a)
            else:
                raise Exception("Error: You can't add edges if one node is missing")
        else:
            raise ValueError("{} is not a tuple".format(a))

    def contains(self, c):
        return c in self._edges or c in self._nodes

    def add_edges(self, edges):
        for e in edges:
            self.add_edge(e)


    def add_nodes(self, nodes):
        for n in nodes:
            self.add_node(n)

    def get_nodes(self):
        return self._nodes

    def get_edges(self):
        return self._edges

    def next(self,n):
        return [k for (n,k) in self.outgoing_edges(n)]


    def outgoing_edges(self,n):
        if n in self.__nodes:
            return [(n1,n2)  for (n1,n2) in self._edges if n1 == n]
        else:
            raise Exception("Error: node not found")

    def ingoing_edges(self,n):
        if n in self.__nodes:
            return [(n1,n2)  for (n1,n2) in self._edges if n2 == n]
        else:
            raise Exception("Error: node not found")


    def __str__(self):
        out =  "Nodes :{}\n".format(self._nodes)
        out += "Edges: "
        for e in self._edges:
            out += "{}\n       ".format(e)
        return out


def main():
    links = [(1,2),(2,3),(3,4),(6,7),(7,5),(1,3)]
    gr = Graph()
    gr.add_nodes([n for (n,k) in links])
    gr.add_nodes([k for (n,k) in links])
    gr.add_edges(links)
    print(gr)
    print("Outgoing edges for {}: {}".format(1,gr.outgoing_edges(1)))
    print("Ingoing edges for {}: {}".format(2,gr.ingoing_edges(2)))
    print("Nodes next to {}: {}".format(1,gr.next(1)))
    print("Graph contains {}: {}".format(1,gr.contains(1)))
    print("Graph contains {}: {}".format((1,2),gr.contains((1,2))))

if __name__=="__main__":
    main()