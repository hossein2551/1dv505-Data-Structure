import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value < self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        elif value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

    def max_depth(self):
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left

            self.value = min_larger_node.value
            self.right = self.right.delete(min_larger_node.value)

        return self

class BstSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root:
            self.root.add(value)
        else:
            self.root = Node(value)

    def delete(self, value):
        if self.root:
            self.root = self.root.delete(value)

    def max_depth(self):
        return self.root.max_depth() if self.root else 0

    def to_dot(self):
        def node_to_dot(node):
            if not node:
                return ""
            dot_text = f'  "{node.value}" [label="{node.value}"]\n'
            if node.left:
                dot_text += f'  "{node.value}" -> "{node.left.value}"\n'
                dot_text += node_to_dot(node.left)
            if node.right:
                dot_text += f'  "{node.value}" -> "{node.right.value}"\n'
                dot_text += node_to_dot(node.right)
            return dot_text

        dot_output = "digraph BST {\n"
        dot_output += node_to_dot(self.root)
        dot_output += "}"
        return dot_output

def simulate_random_deletions():
    num_elements = 1023
    bst = BstSet()

    elements = random.sample(range(num_elements * 10), num_elements)
    for elem in elements:
        bst.add(elem)

    with open("before_delete.txt", "w") as f:
        f.write(bst.to_dot())

    for _ in range(2000):
        to_delete = random.sample(elements, 512)
        for val in to_delete:
            bst.delete(val)

        for val in to_delete:
            bst.add(val)

    with open("after_delete.txt", "w") as f:
        f.write(bst.to_dot())
simulate_random_deletions()
