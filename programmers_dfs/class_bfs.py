from queue import Queue
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
# Class which represents unweighted, undirected graph
class Graph():
    def __init__(self, num_node):
        self.num_node = num_node # the number of nodes
        self.adjacent_list = [[] for _ in range(num_node)]
 
    # add an edge for both nodes
    def add_edge(self, start, end):
        self.adjacent_list[start].append(end)
        self.adjacent_list[end].append(start)
 
 
# visit nodes by DFS using recursion
def DFS(graph, current_node, visited):
    visited[current_node] = True
    print(current_node, end=" ")
    for neighbor in graph.adjacent_list[current_node]:
        if not visited[neighbor]:
            DFS(graph, neighbor, visited)
 
 
# visit nodes by BFS using queue
def BFS(graph, start_node):
    queue = Queue()
    visited = [False for _ in range(graph.num_node)]
    visited[start_node] = True
    queue.put(start_node)
 
    while not queue.empty():
        current_node = queue.get()
        print(current_node, end=' ')
        for neighbor in graph.adjacent_list[current_node]:
            if not visited[neighbor]:
                queue.put(neighbor)
                visited[neighbor] = True
 
 
if __name__ == '__main__':
    # input three integers: the number of nodes, the number of edges,
    # the node from which we start a traversal.
    # Note that we number nodes from 0 to (num_node - 1).
    # num_node, num_edge, start_node = map(int, input().split())
    
    
    for ticket in tickets:
        num_node, num_edge, start_node = , 9, 0 
        graph = Graph(num_node)
    # num_node, num_edge, start_node = 10, 9, 0 
    # graph = Graph(num_node)
    # input an edge with two numbers of nodes in each line
    # for _ in range(num_edge):
    for i in range(num_edge):
        # edge_start, edge_end = map(int, input().split())
        edge_start, edge_end = i, i+1
        graph.add_edge(edge_start, edge_end)
 
    # print results
    print("DFS: ", end="")
    DFS(graph, start_node, visited=[False for _ in range(graph.num_node)])
    print("\nBFS: ", end="")
    BFS(graph, start_node)
    print()