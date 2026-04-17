


class Heap:
    
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def get_size(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.array[0]

    def add(self, elem):
        self.array.append(elem)
        self._heapify_up(len(self.array) - 1)

    def pull_high(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        top = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self._heapify_down(0)
        return top

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.array[index] > self.array[parent]:
            self.array[index], self.array[parent] = self.array[parent], self.array[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.array) and self.array[left] > self.array[largest]:
            largest = left
        if right < len(self.array) and self.array[right] > self.array[largest]:
            largest = right
        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self._heapify_down(largest)

    def __iter__(self):
        return iter(self.array)
