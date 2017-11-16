import node
from node import Node

class DoublyLinkedList:

    def __init__(self):
        self.head = None
    
    def get_list(self):
        current = self.head
        data_set = []
        while current != None:
            data_set.append(current.get_data())
            current = current.get_next()

        return data_set

    def is_empty(self):
        return self.head == None
    
    def search(self, item):
        current = self.head
        while current != None and current.data != item:
            current = current.get_next()
        
        return current 
    
    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
    
    def delete(self, item):
        current = self.search(item)
        if current:
            if current.get_prev():
                current.get_prev().set_next(current.get_next())
            else:
                if current.get_next(): # Is a head 
                    current.get_next().set_prev(None)
                self.head = current.get_next()
            if current.get_next():
                current.get_next().set_prev(current.get_prev())
    
    

    
l = DoublyLinkedList()
l.add(4)
l.add(3)
l.add(2)
l.add(1)
l.delete(1)
l.delete(2)
l.delete(3)
l.delete(4)
print(l.get_list())