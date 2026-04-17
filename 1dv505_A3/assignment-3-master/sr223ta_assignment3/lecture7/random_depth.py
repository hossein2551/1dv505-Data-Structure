
import random
import matplotlib.pyplot as plt
import math

class BstNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, val):
        if val < self.value:
            if self.left is None:
                self.left = BstNode(val)
            else:
                self.left.add(val)
        elif val > self.value:
            if self.right is None:
                self.right = BstNode(val)
            else:
                self.right.add(val)

    def max_depth(self):
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)

class BstSet:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = BstNode(val)
        else:
            self.root.add(val)

    def max_depth(self):
        if self.root is None:
            return 0
        return self.root.max_depth()

def create_bst(elements):
    bst = BstSet()
    for el in elements:
        bst.add(el)
    return bst

def calculate_mean_max_depth(n_elements):
    depths = []
    for _ in range(10):  
        elements = random.sample(range(1, n_elements * 2), n_elements)  
        bst = create_bst(elements)
        depths.append(bst.max_depth())
    return sum(depths) / len(depths)

def complete_tree_depth(n_elements):
    return math.floor(math.log2(n_elements)) + 1

def plot_depth_vs_size():
    sizes = [2**h - 1 for h in range(5, 21)] 
    mean_depths = []
    complete_depths = []

    for size in sizes:
        mean_depth = calculate_mean_max_depth(size)
        complete_depth = complete_tree_depth(size)
        mean_depths.append(mean_depth)
        complete_depths.append(complete_depth)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, mean_depths, label="Average Max Depth", marker='o')
    plt.plot(sizes, complete_depths, label="Complete Tree Depth", linestyle="--", marker='x')
    plt.xlabel("Tree Size")
    plt.ylabel("Max Depth")
    plt.legend()
    plt.title("Tree Sizes vs Average Max Depth and Complete Tree Depth")
    plt.grid(True)
    plt.show()

    log_sizes = [math.log2(size) for size in sizes]
    plt.figure(figsize=(10, 6))
    plt.plot(log_sizes, mean_depths, label="Average Max Depth", marker='o')
    plt.plot(log_sizes, complete_depths, label="Complete Tree Depth", linestyle="--", marker='x')
    plt.xlabel("Log2(Tree Size)")
    plt.ylabel("Max Depth")
    plt.legend()
    plt.title("Log2(Tree Size) vs Average Max Depth and Complete Tree Depth")
    plt.grid(True)
    plt.show()

plot_depth_vs_size()
