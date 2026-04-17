


class BstNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def add(self, val):
        if val < self.value:
            if self.left is None:
                self.left = BstNode(val, None, None)
            else:
                self.left.add(val)
        elif val > self.value:
            if self.right is None:
                self.right = BstNode(val, None, None)
            else:
                self.right.add(val)

    def __str__(self):
        txt = ""
        if self.left is not None:
            txt += self.left.__str__()
        txt += str(self.value) + " "
        if self.right is not None:
            txt += self.right.__str__()
        return txt

    def search(self, val):
        if self.value == val:
            return True
        elif val < self.value and self.left is not None:
            return self.left.search(val)
        elif val > self.value and self.right is not None:
            return self.right.search(val)
        return False
        

    def count(self):
        count_left = self.left.count() if self.left else 0
        count_right = self.right.count() if self.right else 0
        return 1 + count_left + count_right
        

    def count_internal(self):
        count_left = self.left.count_internal() if self.left else 0
        count_right = self.right.count_internal() if self.right else 0
        return (1 if self.left or self.right else 0) + count_left + count_right
        

    def max_depth(self):
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)

    def lr_inorder(self, lst):
        if self.left is not None:
            self.left.lr_inorder(lst)
        lst.append(self.value)
        if self.right is not None:
            self.right.lr_inorder(lst)
        

    def rl_postorder(self, lst):
        if self.right is not None:
            self.right.rl_postorder(lst)
        lst.append(self.value)
        if self.left is not None:
            self.left.rl_postorder(lst)


    def dot(self, parent):

        dot_result = "" 
        if parent is not None:
            dot_result += f'   "{parent}" -- "{self.value}";\n'
    
        if self.left is not None:
            dot_result += self.left.dot(self.value) 
        if self.right is not None:
            dot_result += self.right.dot(self.value)  
    
        return dot_result
    
    def delete(self, value, parent):
        if value < self.value:
             if self.left is not None:
                self.left = self.left.delete(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value, self)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                max_node = self.left
                while max_node.right is not None:
                    max_node = max_node.right
                self.value = max_node.value
                self.left = self.left.delete(max_node.value, self)
        return self

class BstSet:

    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = BstNode(val, None, None)
        else:
            self.root.add(val)

    def __str__(self):
        txt = "{ "
        if self.root is not None:
            txt += self.root.__str__()
        return txt + "}"

    def search(self, val):
        if self.root is None:
            return False
        else:
            return self.root.search(val)
        
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    def count_internal(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_internal()
        
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    def lr_inorder(self):
        lst = []
        if self.root is not None:
            self.root.lr_inorder(lst)
        return lst

    def rl_postorder(self):
        lst = []
        if self.root is not None:
            self.root.rl_postorder(lst)
        return lst

    def delete(self, val):
        if self.root is None:
            return False

        if self.root.value == val:  
            if self.root.left is None:
                if self.root.right is None:
                    self.root = None
                    return True
                else:      
                    self.root = self.root.right  
        return self.root.delete(val, None)

    def dot(self):
        if self.root is None:
            return "No nodes ==> no graph markup"
        else:
            dot_text = "graph BST {\n"
            dot_text += self.root.dot(None) 
            dot_text += "}"
            return dot_text
    

 


        



        

