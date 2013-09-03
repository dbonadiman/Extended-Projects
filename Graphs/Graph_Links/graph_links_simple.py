def __init_graph(maximum):
    return [[0 for j in range(0,maximum+1)] for i in range(0,maximum+1)]



def graph(links):    
    m =  max(max(n for (n,k) in links),max(k for (n,k) in links))
    graph = __init_graph(m)
    for (n,k) in links:
        graph[n][k] = 1
    return graph

def print_matrix(m):
    for l in m:
        print(l)


def main():
    links = [(1,2),(2,3),(5,6),(7,8)]
    print_matrix(graph(links))

if __name__=="__main__":
    main()