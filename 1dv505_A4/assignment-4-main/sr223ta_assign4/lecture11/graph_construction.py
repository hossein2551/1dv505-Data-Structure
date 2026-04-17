class WeightedGraph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices  
        self.edges = edges        

    def printNumberOfVertices(self):
        print(f"Number of vertices: {len(self.vertices)}")

    def printVertexByIndex(self, index):
        if index < len(self.vertices):
            print(f"Vertex at index {index}: {self.vertices[index]}")
        else:
            print("Index out of range")

    def printWeightedEdges(self):
        if not self.edges:
            print("No edges in the graph.")
        else:
            printed_edges = set()
            for u, v, weight in self.edges:
                edge = tuple(sorted([self.vertices[u], self.vertices[v]]))
                if edge not in printed_edges:
                    print(f"{self.vertices[u]} <-> {self.vertices[v]} with weight {weight}")
                    printed_edges.add(edge) 

vertices = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Zebra', 'Monkey', 'Panda', 'Kangaroo', 'Penguin', 'Flamingo', 'Rhino', 'Hippo']
edges = [
    [0, 1, 3], [0, 2, 2], [0, 4, 4], [1, 0, 3], [1, 5, 5], [1, 6, 2], [2, 0, 2], [2, 3, 4], [2, 10, 6], [2, 11, 3], 
    [3, 2, 4], [3, 4, 5], [3, 9, 2], [4, 0, 4], [4, 3, 5], [4, 7, 3], [5, 1, 5], [5, 6, 4], [5, 8, 3], [6, 1, 2], 
    [6, 5, 4], [6, 7, 6], [6, 9, 1], [7, 4, 3], [7, 6, 6], [7, 8, 5], [8, 5, 3], [8, 7, 5], [8, 9, 4], [9, 3, 2], 
    [9, 6, 1], [9, 8, 4], [10, 2, 6], [10, 11, 5], [11, 2, 3], [11, 10, 5]
]

graph = WeightedGraph(vertices, edges)

graph.printNumberOfVertices()
graph.printVertexByIndex(2)
graph.printWeightedEdges()
