import treenode 
from treenode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent = current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
                
    def __setitem__(self, k, v):
        self.put(k, v)

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
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)
        
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        if self._get(key, self.root):
            return true
        else:
            return False
    
    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")
    
    def __delitem__(self, key):
        self.delete(key)
    
    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            succ = current_node.successor 
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent 
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                    current_node.left_child.payload,
                                    current_node.left_child.left_child,
                                    current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current.node.right_child.parent =current_node.parent 
                    current_node.parent.left_child = current.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent 
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                    current_node.right_child.payload,
                                    current_node.right_child.left_child,
                                    current_node.right_child.right_child)

    def inorder(self):
        current_node = self.root
        if current_node:
            while current_node.has_left_child():
                current_node = current_node.left_child
            while current_node:
                print(current_node.get_val())
                current_node = current_node.successor

my_tree = BinarySearchTree()
my_tree[5] = 5
my_tree[4] = 4
my_tree[6] = 6
my_tree[3] = 3
my_tree[7] = 7
# print(my_tree[6])
# print(my_tree[2])
# print(my_tree.root.get_val())
# print(my_tree.root.right_child.get_val())
# print(my_tree.root.left_child.get_val())
(my_tree.inorder())