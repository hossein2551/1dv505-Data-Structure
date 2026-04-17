


class QuadHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.count = 0

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def next_prime(self, n):
        while not self.is_prime(n):
            n += 1
        return n

    def resize(self):
        new_size = self.next_prime(self.size * 2)
        old_table = self.table
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        if self.count / self.size > 0.5:
            self.resize()
        
        index = self.hash_function(key)
        i = 0
        for i in range(self.size):
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = (key, value)
                self.count += 1
                return
            elif self.table[new_index][0] == key:
                self.table[new_index] = (key, value)
                return

    def search(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                return None
            elif self.table[new_index][0] == key:
                return self.table[new_index][1]

    def delete(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                return
            elif self.table[new_index][0] == key:
                self.table[new_index] = None
                self.count -= 1
                return

ht = QuadHash(7)
ht.insert("Kiwi", 10)
ht.insert("Annanas", 20)
ht.insert("watermelon", 30)

print("Search Kiwi:", ht.search("Kiwi"))  
print("Search Annanas:", ht.search("Annanas"))  

ht.delete("Annanas")
print("Search Annanas after delete:", ht.search("Annanas"))
