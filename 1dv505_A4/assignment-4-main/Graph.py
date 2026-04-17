from Queue import Queue
from Tree import Tree

class Graph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.neighbors = self.getAdjacencyLists(edges)

    def getAdjacencyLists(self, edges):
        neighbors = [[] for _ in range(len(self.vertices))]
        for u, v in edges:
            neighbors[u].append(Edge(u, v))
        return neighbors

    def getSize(self):
        return len(self.vertices)

    def getVertices(self):
        return self.vertices

    def getVertex(self, index):
        return self.vertices[index]

    def getIndex(self, v):
        return self.vertices.index(v)

    def getNeighbors(self, index):
        return self.neighbors[index]

    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

    def printEdges(self):
        for u, neighbors in enumerate(self.neighbors):
            print(f"{self.getVertex(u)} -->", end=" ")
            for edge in neighbors:
                print(f"({u}, {edge.v})", end=" ")
            print()

    def clear(self):
        self.vertices = []
        self.neighbors = []

    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.neighbors.append([])

    def addEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
            self.neighbors[indexU].append(Edge(indexU, indexV))

    def dfs(self, v):
        searchOrders = []
        parent = [-1] * len(self.vertices)
        isVisited = [False] * len(self.vertices)
        self.dfsHelper(v, parent, searchOrders, isVisited)
        return Tree(v, parent, searchOrders, self.vertices)

    def dfsHelper(self, v, parent, searchOrders, isVisited):
        searchOrders.append(v)
        isVisited[v] = True
        for e in self.neighbors[v]:
            w = e.v
            if not isVisited[w]:
                parent[w] = v
                self.dfsHelper(w, parent, searchOrders, isVisited)

    def bfs(self, v):
        searchOrders = []
        parent = [-1] * len(self.vertices)
        queue = Queue()
        isVisited = [False] * len(self.vertices)
        queue.enqueue(v)
        isVisited[v] = True

        while not queue.isEmpty():
            u = queue.dequeue()
            searchOrders.append(u)
            for e in self.neighbors[u]:
                w = e.v
                if not isVisited[w]:
                    queue.enqueue(w)
                    isVisited[w] = True
                    parent[w] = u

        return Tree(v, parent, searchOrders, self.vertices)

class Edge:
    def __init__(self, u, v):
        self.u = u 
        self.v = v  