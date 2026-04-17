class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        self.root = root
        self.parent = parent
        self.searchOrders = searchOrders
        self.vertices = vertices

    def getRoot(self):
        return self.root

    def getParent(self, index):
        return self.parent[index]

    def getSearchOrders(self):
        return self.searchOrders

    def getNumberOfVerticesFound(self):
        return len(self.searchOrders)

    def getPath(self, index):
        path = []
        while index != -1:
            path.append(self.vertices[index])
            index = self.parent[index]
        return path

    def printPath(self, index):
        path = self.getPath(index)
        print("A path from " + str(self.vertices[self.root]) + " to "
              + str(self.vertices[index]) + ": ", end="")
        for i in range(len(path) - 1, -1, -1):
            print(path[i], end=" ")

    def printTree(self):
        print("Root is: " + str(self.vertices[self.root]))
        print("Edges: ", end="")

        for i in range(len(self.parent)):
            if self.parent[i] != -1:
                print("(" + str(self.vertices[self.parent[i]]) +
                      ", " + str(self.vertices[i]) + ")", end=" ")
        print()
