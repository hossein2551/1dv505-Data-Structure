from Graph import Graph  
from Tree import Tree  

vertices = ["A", "B", "C", "D", "E"]
edges = [(0, 1), (0, 2), (1, 3), (1, 4)]


g = Graph(vertices, edges)

tree = g.bfs(0)

if tree:
    search_orders = [vertices[i] for i in tree.getSearchOrders()]
    print("Search order:", search_orders)
    
    parent_array = [tree.getParent(i) for i in range(len(vertices))]
    print("Parent array:", parent_array)
else:
    print("Noden hittades inte.")