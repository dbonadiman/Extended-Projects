from copy import deepcopy


def strong_connectivity(graph, node):
	return strong_connectivity_r(deepcopy(graph),[1]*len(graph),[node],sum(sum(x for x in i) for i in graph))	
 	


def strong_connectivity_r(visited, nodes, path, edges_left):	
	if len(path)>1 :
		visited[path[-2]][path[-1]]=0
	nodes[path[-1]] = 0
	for j in range(0,len(nodes)):
		if visited[path[-1]][j]:
			out = strong_connectivity_r(deepcopy(visited),nodes,deepcopy(path+[j]),edges_left-1)
			if out:
				return out
	if sum(x for x in nodes)==0:
		return True
	return False


def connected(graph):
	strong_connectivity(graph,0)

def print_matrix(m):
	for l in m:
		print l

def main():
	graph = [[0,1,0,0],
			 [1,0,0,0],
			 [0,0,0,1],
			 [0,0,1,0]]
	print_matrix(graph)
	print "\n Connected:{}\n".format(connected(graph))
	graph = [[0,1,0,0],
			 [0,0,1,0],
			 [0,0,0,1],
			 [1,0,0,0]]
	print_matrix(graph)
	print "\n Connected:{}\n".format(connected(graph))
	graph = [[0,1,0,1],
		 	[0,0,1,0],
		 	[1,0,0,0],
		 	[0,0,0,0]]
	print_matrix(graph)
	print "\n Connected:{}\n".format(connected(graph))
	graph = [[0,0,0,0],
			 [0,0,0,0],
			 [0,0,0,0],
			 [0,0,0,0]]
	print_matrix(graph)
	print "\n Connected:{}\n".format(connected(graph))
	graph = [[1,1,1,1],
			 [1,1,1,1],
			 [1,1,1,1],
			 [1,1,1,1]]
	print_matrix(graph)
	print "\n Connected:{}\n".format(connected(graph))


if __name__=="__main__":
	main()