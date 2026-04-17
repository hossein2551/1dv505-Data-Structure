


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def add_last(self, n):
        new = Node(n, None)
        if self.head is None:  
            self.head = new
            self.tail = new
        else:
            self.tail.nxt = new
            self.tail = new
        self.size += 1

  
    def add_first(self, n):
        new = Node(n, self.head)
        if self.head is None: 
            self.tail = new
        self.head = new
        self.size += 1


    def get_last(self):
        if self.is_empty():
            raise IndexError("Accessing an emoty queue is not possible")
        return self.tail.value


    def get_first(self):
        if self.is_empty():
            raise IndexError("Accessing an emoty queue is not possible")
        return self.head.value


    def remove_first(self):
        if self.is_empty():
            raise IndexError("Removing from an empty queue is not possible")
        value = self.head.value
        self.head = self.head.nxt
        if self.head is None:  
            self.tail = None
        self.size -= 1
        return value


    def remove_last(self):
        if self.is_empty():
            raise IndexError("Accessing an emoty queue is not possible")
        

        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
           

            current = self.head
            while current.nxt != self.tail:
                current = current.nxt
            value = self.tail.value
            self.tail = current
            self.tail.nxt = None
        
        self.size -= 1
        return value


    def is_empty(self):
        return self.size == 0


    def __str__(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s


    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.nxt
