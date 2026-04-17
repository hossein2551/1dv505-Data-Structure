class WeightedGraph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = self.getAdjacencyLists(edges)

    def getAdjacencyLists(self, edges):
        adjacency_list = {vertex: [] for vertex in self.vertices}
        for edge in edges:
            start, end, weight = edge
            adjacency_list[self.vertices[start]].append((self.vertices[end], weight))
            adjacency_list[self.vertices[end]].append((self.vertices[start], weight))
        return adjacency_list

    def printWeightedEdges(self):
        printed_edges = set()  

        for start, end, weight in self.edges:
            edge = tuple(sorted([self.vertices[start], self.vertices[end]]))

            if edge not in printed_edges:
                print(f"{edge[0]} <-> {edge[1]} with weight {weight}")
                printed_edges.add(edge)  
     def getWeight(self, u, v):
        for edge in self.edges:
            start, end, weight = edge
            if (self.vertices[start] == u and self.vertices[end] == v) or (self.vertices[start] == v and self.vertices[end] == u):
                return weight
        return None

    def addEdge(self, u, v, w):
        start_index = self.vertices.index(u)
        end_index = self.vertices.index(v)
        self.edges.append([start_index, end_index, w])
        self.adjacency_list = self.getAdjacencyLists(self.edges)

    def getMinimumSpanningTree(self, startingVertex=0):
        pass

    def getShortestPath(self, sourceVertex):
        pass
