class WeightedGraph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.edges = edges
        self.adj_list = self.getAdjacencyLists(edges)

    def getAdjacencyLists(self, edges):
        adj_list = {vertex: [] for vertex in self.vertices}
        for u, v, w in edges:
            adj_list[self.vertices[u]].append((self.vertices[v], w))
            adj_list[self.vertices[v]].append((self.vertices[u], w))  
        return adj_list

    def printWeightedEdges(self):
        for u, v, w in self.edges:
            print(f"{self.vertices[u]} <-> {self.vertices[v]} with weight {w}")
    def getMinimumSpanningTree(self, startingVertex=0):
        mst_edges = []
        visited = [False] * len(self.vertices)
        visited[startingVertex] = True

        while len(mst_edges) < len(self.vertices) - 1:
            min_edge = None
            min_weight = float('inf')

            for i in range(len(self.vertices)):
                if visited[i]:  
                    for neighbor, weight in self.adj_list[self.vertices[i]]:
                        j = self.vertices.index(neighbor)
                        if not visited[j] and weight < min_weight:
                            min_weight = weight
                            min_edge = (i, j, weight)
            if min_edge:
                mst_edges.append(min_edge)
                visited[min_edge[1]] = True

        return mst_edges

    def getShortestPath(self, sourceVertex):
        n = len(self.vertices)
        distances = [float("inf")] * n
        previous = [None] * n
        distances[sourceVertex] = 0
        visited = [False] * n

        while not all(visited):
            min_distance = float("inf")
            min_vertex = None
            for i in range(n):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    min_vertex = i

            visited[min_vertex] = True

            for neighbor, weight in self.adj_list[self.vertices[min_vertex]]:
                neighbor_index = self.vertices.index(neighbor)
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor_index]:
                    distances[neighbor_index] = new_distance
                    previous[neighbor_index] = min_vertex

        shortest_paths = {}
        for vertex in range(n):
            path = []
            current = vertex
            while current is not None:
                path.append(self.vertices[current])
                current = previous[current]
            shortest_paths[self.vertices[vertex]] = path[::-1] 

        return shortest_paths, distances
    
vertices = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Zebra', 'Monkey', 'Panda', 'Kangaroo', 'Penguin', 'Flamingo', 'Rhino', 'Hippo']
edges = [
    (0, 1, 3), (0, 2, 2), (0, 4, 4),
    (1, 0, 3), (1, 5, 5), (1, 6, 2),
    (2, 0, 2), (2, 3, 4), (2, 10, 6), (2, 11, 3),
    (3, 2, 4), (3, 4, 5), (3, 9, 2),
    (4, 0, 4), (4, 3, 5), (4, 7, 3),
    (5, 1, 5), (5, 6, 4), (5, 8, 3),
    (6, 1, 2), (6, 5, 4), (6, 7, 6), (6, 9, 1),
    (7, 4, 3), (7, 6, 6), (7, 8, 5),
    (8, 5, 3), (8, 7, 5), (8, 9, 4),
    (9, 3, 2), (9, 6, 1), (9, 8, 4),
    (10, 2, 6), (10, 11, 5),
    (11, 2, 3), (11, 10, 5)
]
graph = WeightedGraph(vertices, edges)

mst = graph.getMinimumSpanningTree(startingVertex=0)
print("Minimum Spanning Tree (MST):")
for u, v, w in mst:
    print(f"{vertices[u]} <-> {vertices[v]} with weight {w}")

shortest_paths, distances = graph.getShortestPath(sourceVertex=0)
print("\nShortest Path from Lion:")
for vertex, path in shortest_paths.items():
    print(f"Path to {vertex}: {' -> '.join(path)} (Distance: {distances[vertices.index(vertex)]})")
