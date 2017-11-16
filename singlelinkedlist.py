import node
from node import Node 


class SingleLinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None
    
    def get_list(self):
        data_set = []
        current = self.head 
        while current != None:
            data_set.append(current.data)
            current = current.get_next()
        
        return data_set
        
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    
    def delete(self, item):
        current = self.head
        previous = None
        found = False
        if current != None:
            while not found:
                if current.get_data() == item:
                    found = True
                else:
                    previous = current
                    current = current.get_next()
            
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    
    def search(self, item):
        current = self.head 
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.get_next()
        
        return found
    
    def reverse(self):
        current = self.head 
        prev = None
        while current:
            temp = current.next 
            current.next = prev
            prev = current 
            current = temp 
            if current:
                self.head = current 

    # def pop(self):
    #     current = self.head 
    #     data = current.data
    #     if current:
    #         self.head = self.head.get_next()

    #     return data


# l = SingleLinkedList()
# l.add(1)
# l.add(2)
# l.add(3)
# l.add(4)
# l.add(5)
# l.add(6)
# l.add(7)
# print(l.get_list())
# l.reverse()
# print(l.get_list())
# l.delete(1)
# print(l.get_list())
# l.delete(4)
# print(l.get_list())
# l.delete(7)
# print(l.get_list())
# l.delete(5)
# print(l.get_list())
# # l.append(100)
# # print(l.get_list())
