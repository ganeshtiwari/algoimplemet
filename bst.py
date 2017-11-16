import bstnode
from bstnode import Node 


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, key, val):
        node_to_insert = Node(key, val)
        self._insert(node_to_insert)

    def _insert(self, node_to_insert): # T. Cormann 
        parent = None 
        current_node = self.root
        while current_node != None:
            parent = current_node # Track parent node 
            if node_to_insert.key < current_node.key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        node_to_insert.parent = parent 
        if parent == None:
            self.root = node_to_insert # Tree was empty # Not now :P 
        else:
            if node_to_insert.key < parent.key:
                parent.left_child = node_to_insert
            else:
                parent.right_child = node_to_insert
        
    def __setitem__(self, key, val):
        self.insert(key, val)
    
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    
    def _get(self, key, current_node):
        if current_node == None:
            return None
        elif key == current_node.key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)
        
    def __getitem__(self, key):
        return self.get(key)

    def inorder_traverse(self):
        current = self.root
        while current.has_left_child():
            current = current.left_child
        while current:
            print(current.payload)
            current = current.find_successor()
                # pass
    def delete(self, key): # T. Cormann fuck you 
        node_to_delete = self._get(key, self.root)
        if node_to_delete:
            self._delete(node_to_delete)
        else:
            raise KeyError("I saw this coming. Am I am wizard. :P")
    
    def _delete(self, node_to_delete):
        if node_to_delete.is_leaf(): # Just remove it # Don't act smart 
            if node_to_delete.is_left_child():
                node_to_delete.parent.left_child = None
            else:
                node_to_delete.parent.right_child = None 
        elif node_to_delete.has_any_child(): # If has_child # Kill it # Child is dangerous #Especially two child. # Deal abstractly LOL
            succ = node_to_delete.find_successor()
            succ.splice_out()
            node_to_delete.replace_node_data(succ.key,
                                            succ.payload,
                                            succ.left_child,
                                            succ.right_child
            )
    def __delitem__(self, k):
        self.delete(key)

    # def delete(self, key):
    #     node_to_delete = self._get(key, self.root)
    #     if self.size > 1:
    #         if node_to_delete:
    #             self.size -= 1
    #             self._remove(node_to_delete)
    #         else:
    #             raise KeyError
    #     elif self.size == 1 and key == self.root.key:
    #         self.root = None
    #         self.size -= 1
    #     else:
    #         raise KeyError
    
    # def _remove(self, node_to_delete):
    #     if node_to_delete.is_leaf():
    #         if node_to_delete.is_left_child():
    #             node_to_delete.parent.left_child = None 
    #         else:
    #             node_to_delete.parent.right_child = None
    #     else:
    #         if node_to_delete.has_left_child():
    #             if node_to_delete.is_left_child():
    #                 node_to_delete.parent.left_child = node_to_delete.left_child
    #                 node_to_delete.left_child.parent = node_to_delete.parent
    #             elif node_to_delete.is_right_child():
    #                 node_to_delete.parent.right_child = node_to_delete.left_child 
    #                 node_to_delete.left_child.parent = node_to_delete.parent 
    #             else:
    #                 node_to_delete.replace_node_data(node_to_delete.left_child.key, 
    #                                                 node_to_delete.left_child.payload,
    #                                                 node_to_delete.left_child.left_child,
    #                                                 node_to_delete.left_child.right_child
    #                 )
    #         else:
    #             if node_to_delete.is_left_child():
    #                 node_to_delete.parent.left_child = node_to_delete.right_child
    #                 node_to_delete.right_child.parent = node_to_delete.parent
    #             elif node_to_delete.is_right_child():
    #                 node_to_delete.parent.right_child = node_to_delete.right_child
    #                 node_to_delete.right_child.parent = node_to_delete.parent
    #             else:
    #                 node_to_delete.replace_node_data(node_to_delete.right_child.key, 
    #                                                 node_to_delete.right_child.payload,
    #                                                 node_to_delete.right_child.left_child,
    #                                                 node_to_delete.right_child.right_child
    #                 )
        
    # def delete(self, key): # From intro algo book 
    #     node_to_delete = self._get(key, self.root)
    #     if node_to_delete:
    #         self.size -= 1
    #         self._delete(node_to_delete)
    
    # def _delete(self, node_to_delete): #From T. Cormann 
    #     if node_to_delete.left_child == None or node_to_delete.right_child == None:
    #         y = node_to_delete
    #     else:
    #         y = node_to_delete.find_successor()
    #     if y.left_child:
    #         x = y.left_child
    #     else:
    #         x = y.right_child
    #     if x:
    #         x.parent = y.parent 
    #     if y.parent == None:
    #         self.root = x
    #     elif y == y.parent.left_child:
    #         y.parent.left_child = x
    #     else:
    #         y.parent.right_child = x
    #     if y != node_to_delete:
    #         node_to_delete.replace_node_data(y.key, y.payload, y.left_child, y.right_child)



my_tree = BinarySearchTree()
my_tree[12] = 12
my_tree[5] = 5
my_tree[18] = 18
# my_tree[6] = "yellow"
my_tree[2] = 2
my_tree[9] = 9
my_tree[15] = 15
my_tree[19] = 19
my_tree[13] = 13
my_tree[17] = 17
# print(my_tree[6])
# print(my_tree[2])
# print(my_tree.root.get_val())
# print(my_tree.root.right_child.get_val())
# print(my_tree.root.left_child.get_val())
# print(my_tree.get(7))
my_tree.delete(15)
my_tree.inorder_traverse()