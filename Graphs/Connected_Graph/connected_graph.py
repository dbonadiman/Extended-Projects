from copy import deepcopy


def strong_connectivity(graph, node):
	if graph in [[],[[1]],[[0]]]:
		return True
	else:
		return strong_connectivity_r(deepcopy(graph),[1]*len(graph),[node],sum(sum(x for x in i) for i in graph))	
 	


def strong_connectivity_r(visited, nodes, path, edges_left):
	if len(path)>1 :
		visited[path[-2]][path[-1]]=0
	nodes[path[-1]] = 0
	if sum(x for x in nodes)==0:
		return True
	for j in range(0,len(nodes)):
		if visited[path[-1]][j]:
			if nodes[j]:
				out = strong_connectivity_r(deepcopy(visited),nodes,deepcopy(path+[j]),edges_left-1)
				if out:
					return out
	for j in range(0,len(nodes)):
		if visited[path[-1]][j]:
			if not nodes[j]:
				out = strong_connectivity_r(deepcopy(visited),nodes,deepcopy(path+[j]),edges_left-1)
				if out:
					return out
	return False


def connected(graph):
	return strong_connectivity(graph,0)

def print_matrix(m):
	for l in m:
		print l

def main():

	graph = [[0,1,0,0],
			 [1,0,0,0],
			 [0,0,0,1],
			 [0,0,1,0]]
	print_matrix(graph)
	print "\n Connected: {}\n".format(connected(graph))
	graph = [[0,1,0,0],
			 [0,0,1,0],
			 [0,0,0,1],
			 [1,0,0,0]]
	print_matrix(graph)
	print "\n Connected: {}\n".format(connected(graph))
	graph = [[0,1,0,1],
		 	[0,0,1,0],
		 	[1,0,0,0],
		 	[0,0,0,0]]
	print_matrix(graph)
	print "\n Connected: {}\n".format(connected(graph))
	graph = [[0,0,0,0],
			 [0,0,0,0],
			 [0,0,0,0],
			 [0,0,0,0]]
	print_matrix(graph)
	print "\n Connected: {}\n".format(connected(graph))
	graph = [[1,1,1,1],
			 [1,1,1,1],
			 [1,1,1,1],
			 [1,1,1,1]]
	print_matrix(graph)
	print "\n Connected: {}\n".format(connected(graph))
	graph = []
	print_matrix(graph)
	print "\n Connected: {}\n".format(connected(graph))
	graph = [[1]]
	print_matrix(graph)
	print "\n Connected: {}\n".format(connected(graph))


if __name__=="__main__":
	main()