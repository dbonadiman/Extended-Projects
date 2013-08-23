from copy import deepcopy

def eulerian_path(graph, node):
	result = eulerian_path_r(-1,node,deepcopy(graph),[1 for i in range(0,len(graph))])
	if len(result)>0:
 		if node in result:
 			return "Eulerian Cycle"
 		else:
 			return "Eulerian Path"
 	else:
 		return "Not Eulerian Path"


def eulerian_path_r(node_j, node_i , visited, nodes):	
	if node_j != -1:
		visited[node_j][node_i]=0
	nodes[node_i] = 0
	if sum(sum(x) for x in visited)==0 and sum(x for x in nodes)==0:
		return [node_i]
	if sum(x for x in visited[node_i])==0:
		return []
	output =[]
	for j in range(0,len(visited)):
		if visited[node_i][j]:
			output += eulerian_path_r(node_i,j,deepcopy(visited),nodes)
	return output

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

if __name__=="__main__":
	main()