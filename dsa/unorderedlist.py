import node
from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def is_empty(self):
        return self.head == None
    
    def get_list(self):
        current = self.head
        data_set = []
        while current != None:
            data_set.append(current.get_data())
            current = current.get_next()
        
        return data_set
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.count += 1
        if self.count <= 1:
            self.tail = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        
        return found
    
    def remove(self, item):
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

    def append(self, item):
        current = self.tail
        temp = Node(item)
        if current == None:
            self.head = temp
            self.tail = temp
            temp.set_next(None)
        else:
            current.set_next(temp)
            self.tail = temp
    
    def index(self, item):
        count = 0
        current = self.head
        while current.get_data() != item:
            count += 1
            current = current.get_next()
        
        return count
    
    def pop(self, pos=None):
        current = self.head
        previous = None
        if pos == None or pos == -1: # Default pop (pop from last position)
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            
            if previous != None: # Not the head node
                previous.set_next(None)
                self.tail = previous
            else:
                self.head = None
        elif pos != None: # pop item form the given position
            count = 0
            while pos != count:
                count += 1
                previous = current
                current = current.get_next()

            if previous == None: # Pop item from 0 position
                self.head = current.get_next()
            elif current == None: # Pop item from last position
                previous.set_next(None)
                self.tail = previous
            else: 
                previous.set_next(current.get_next())
    
    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0
        temp = Node(item)
        if pos >= 0:
            while count != pos:
                previous = current
                current = current.get_next()
                count += 1

            if previous == None:  # Inserting at index 0
                temp.set_next(self.head)
                self.head = temp
            elif current == None: # Inserting at the end 
                previous.set_next(temp)
                self.tail = previous
            else: 
                previous.set_next(temp)
                temp.set_next(current)
        else:
            raise IndexError
    
    def slice(self, start, end):
        ls = self.__str__()
        return(ls[start: end])
    
    def __str__(self):
        current = self.head
        data_set = []
        while current != None:
            data_set.append(current.get_data())
            current = current.get_next()
        
        return data_set

u = UnorderedList()
u.add(1)
u.add(2)
u.add(3)
u.add(4)
print(u.get_list())
u.append(100)
print(u.get_list())
u.append(101)
print(u.get_list())
u.pop(0)
print(u.get_list())
u.pop(0)
print(u.get_list())
print(u.slice(0, 3))
# u.remove()