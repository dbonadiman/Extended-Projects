def dijkstra(graph,source_node,destination):
	if len(graph)<1:
		raise ValueError("Graph not Valid")
	nodes = set([i for i in range(len(graph))])
	dist = [0 if i==source_node  else float("inf") for i in nodes]
	previous = [float("inf") for i in nodes]
	while len(nodes)>1:
		val, idx = min((val, idx) for (idx, val) in enumerate(dist) if idx in nodes )
		nodes.discard(idx)
		if val == float("inf"):
			break
		for (i, n) in enumerate(graph[idx]):
			if n > 0:
				 a  = val+graph[idx][i]
				 if a<dist[i]:
					 dist[i] = a
					 previous[i] = idx
	sequence = []
	p = destination
	try:
		while True:
			sequence.append(p)
			p = previous[p]
			if p==source_node:
				break
		sequence.append(source_node)
	except:
		return []
	
	return sequence[::-1]

def print_matrix(m):
	for l in m:
		print(l)

def __main():
	graph = [[0,2,1,0],
			 [0,0,1,0],
			 [0,3,0,1],
			 [1,1,6,0]]
	print_matrix(graph)
	for i in range(len(graph)):
		print("\nThe minimum path from {} to {} are : {}\n".format(i,0,dijkstra(graph,i,0)))
		
	graph = []
	print_matrix(graph)
	try:
		print("\nThe minimum path from {} to {} are : {}\n".format(0,0,dijkstra(graph,0,0)))
	except ValueError:
		print("Graph not Valid")
		
	graph = [[0]]
	print_matrix(graph)
	try:
		print("\nThe minimum path from {} to {} are : {}\n".format(0,0,dijkstra(graph,0,0)))
	except ValueError:
		print("Graph not Valid")
		
		
	graph = [[0,0,0,0],
			 [0,0,0,0],
			 [0,0,0,0],
			 [0,0,0,0]]
	print_matrix(graph)
	for i in range(len(graph)):
		print("\nThe minimum path from {} to {} are : {}\n".format(i,0,dijkstra(graph,i,0)))
	


if __name__=="__main__":
	__main()