class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

    def dfs(self, start_vertex):
        is_visited = [False] * self.vertices
        search_orders = []
        parent = [-1] * self.vertices

        def dfs_recursive(vertex):
            is_visited[vertex] = True
            search_orders.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if not is_visited[neighbor]:
                    parent[neighbor] = vertex
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)

        print("DFS search order:", search_orders)
        print("Parent array:", parent)

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.dfs(0)
