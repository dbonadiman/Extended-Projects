from copy import deepcopy

def eulerian_path(graph, node):
	return eulerian_path_r(deepcopy(graph),[1 for i in range(0,len(graph))],[node],sum(sum(x for x in i) for i in graph))	
 	


def eulerian_path_r(visited, nodes, path, edges_left):	
	if len(path)>1 :
		visited[path[-2]][path[-1]]=0
	nodes[path[-1]] = 0
	for j in range(0,len(nodes)):
		if visited[path[-1]][j]:
			return eulerian_path_r(deepcopy(visited),nodes,deepcopy(path+[j]),edges_left-1)
	if edges_left==0 and sum(x for x in nodes)==0:
		return path
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
	print "\nPath:{}\n".format(eulerian_path(graph,0))
	graph = [[0,1,0,0],
			 [0,0,1,0],
			 [0,0,0,1],
			 [1,0,0,0]]
	print_matrix(graph)
	print "\nPath:{}\n".format(eulerian_path(graph,0))
	graph = [[0,1,0,1],
		 	[0,0,1,0],
		 	[1,0,0,0],
		 	[0,0,0,0]]
	print_matrix(graph)
	print "\nPath:{}\n".format(eulerian_path(graph,0))



if __name__=="__main__":
	main()