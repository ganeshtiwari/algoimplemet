'''
Left - Rotation in RBT

                                x

                    a                       Y 

                                        b       g


                            left rotation

                                Y

                    X                       g

                a       b           



'''

import redblacknode
from redblacknode import Node 

RED = 1
BLACK = 0

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def put(self, key):
        node_to_insert = Node(key=key)
        self.size += 1
        self._put(node_to_insert)
    
    def _put(self, node_to_insert):
        parent = None 
        current_node = self.root
        while current_node:
            parent = current_node
            if key < current_node.key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        
        node_to_insert.parent = parent
        if parent == None:
            self.root = node_to_insert
        else:
            if node_to_insert.key < parent.key:
                parent.left_child = node_to_insert
            else:
                parent.right_child = node_to_insert
        node_to_insert.color = RED
        self.fix_up(node_to_insert)
    
    def fix_up(self, node_to_insert):
        pass
    
    def left_rotate(self, x): # T. Cormann 
        y = x.right_child # Set  y 
        x.right_child = y.left_child # Turn y's left subtree to x's right subtree
        if y.left_child != None:
            y.left_child.parent = x
            x.right_child = y.left_child
        y.parent = x.parent # Link x's parent to y
        if x.parent == None:
            self.root = y
        elif x.is_left_child():
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.left_child = x
        x.parent = y

