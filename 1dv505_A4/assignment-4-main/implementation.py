from Queue import Queue

def bfs(self, start_index):
    queue = Queue()
    visited = [False] * len(self._vertices)
    queue.enqueue(start_index)
    visited[start_index] = True

    while not queue.isEmpty():
        current = queue.dequeue()
        print(f"Visited: {self._vertices[current]}")

        for neighbor in self.getNeighbors(current):
            if not visited[neighbor]:
                queue.enqueue(neighbor)
                visited[neighbor] = True