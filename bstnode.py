class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right 
        self.parent = parent 
    
    def has_left_child(self):
        return self.left_child
    
    def has_right_child(self):
        return self.right_child
    
    def has_any_child(self):
        return self.left_child or self.right_child
    
    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_leaf(self):
        return not (self.left_child or self.right_child)
    
    def has_both_child(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, val, lc, rc): # Fuck you T. Cormann #From G.R. Tiwari 
        self.key = key
        self.payload = val
        if self.has_left_child(): # Retain the left and right child if any
            self.left_child.parent = self
        elif self.has_right_child():
            self.right_child.parent = self
        else: # If not replace left and right nodes 
            self.left_child = lc
            self.right_child = rc

    def find_min(self): # Finds minimum node wrt to current node
        while self.has_left_child():
            self = self.left_child
        
        return self
    
    def find_successor(self): # Finds successor of the current node ie one step greater than current node key
        succ = None
        if self.right_child: # Check the right subtree first 
            return self.right_child.find_min()
        else:
            if self.parent: 
                if self.is_left_child(): # If current node has no right subtree than its parent is the successor only if it is a left child
                    succ = self.parent 
                else: # Not a left child
                    self.parent.right_child = None
                    succ = self.parent.find_successor() # Parents successor is the current node's successorS
                    self.parent.right_child = self
        return succ
    
    def find_max(self): # Finds max node wrt to the current node
        if current_node.has_right_child():
            return self.right_child.find_max()
        else:
            return self

    def find_predecessor(self):
        pass
    
    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_child():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent 
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.right_child.parent = self.parent 
                    