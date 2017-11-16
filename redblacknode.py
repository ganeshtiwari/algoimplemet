class Node:
    def __init__(self, key, color=None, left=None, right=None, parent=None):
        self.color = color 
        self.key = key
        self.left_child = left
        self.right_child = right 
        self.parent = parent 
    
    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def has_left_child(self):
        return self.left_child
    
    def has_right_child(self):
        return self.right_child
    
    def has_any_child(self):
        return self.left_child and self.right_child
    
    def is_leaf(self):
        return not (self.left_child or self.right_child)
    
    def has_both_children(self):
        return self.left_child and self.right_child
    
