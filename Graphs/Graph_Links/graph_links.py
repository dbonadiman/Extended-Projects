class Graph:
	__nodes = []
	__edges = []

	def __init__(self,nodes=[],edges=[]):
		if len(nodes)>0:
			self.add_nodes(n for n in nodes)
		if len(edges)>0:
			self.add_edges(e for e in edges)

	def add_edges(self, edges):
		for (n,k) in edges:
			if (n in self.__nodes) and (k in self.__nodes):
				self.__edges.append((n,k))
			else:
				raise Exception("Error: You can't add edges if one node is missing")


	def add_nodes(self, nodes):
		for n in nodes:
			if n not in self.__nodes:
				self.__nodes.append(n)

	def __str__(self):
		out =  "Nodes :{}\n".format(self.__nodes)
		out += "Edges: "
		for e in self.__edges:
			out += "{}\n       ".format(e)
		return out



def main():
	links = [(1,2),(1,5),(1,10),(3,5)]
	gr = Graph()
	gr.add_nodes((n for (n,k) in links))
	gr.add_nodes((k for (n,k) in links))
	gr.add_edges((e for e in links))
	print gr


if __name__=="__main__":
	main()