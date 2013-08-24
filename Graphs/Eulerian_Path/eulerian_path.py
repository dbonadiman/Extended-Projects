from copy import deepcopy

def eulerian_path(graph, node):
	return eulerian_path_r(node,deepcopy(graph),[1 for i in range(0,len(graph))],[])	
 	


def eulerian_path_r(node_i , visited, nodes, path):	
	if path !=[] :
		visited[path[-1]][node_i]=0
	nodes[node_i] = 0
	path.append(node_i)
	if sum(sum(x) for x in visited)==0 and sum(x for x in nodes)==0:
		return path
	for j in range(0,len(visited)):
		if visited[node_i][j]:
			output = eulerian_path_r(j,deepcopy(visited),nodes,deepcopy(path))
			if output!=[]:
				return output
	return []

def print_matrix(m):
	for l in m:
		print l

def main():
	graph = [[0,1,0,0],
			 [0,0,1,0],
			 [0,0,0,1],
			 [1,0,1,0]]
	print_matrix(graph)
	print eulerian_path(graph,0)
	graph = [[0,1,0,0],
			 [0,0,1,0],
			 [0,0,0,1],
			 [1,0,0,0]]
	print_matrix(graph)
	print eulerian_path(graph,0)
	graph = [[0,1,0,1],
		 	[0,0,1,0],
		 	[1,0,0,0],
		 	[0,0,0,0]]
	print_matrix(graph)
	print eulerian_path(graph,0)
	graph = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		 	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
	print_matrix(graph)
	print eulerian_path(graph,0)


if __name__=="__main__":
	main()