import singlelinkedlist
from singlelinkedlist import SingleLinkedList


class Stack:
    def __init__(self):
        self.items = SingleLinkedList()

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.add(item)
    
    def pop(self):
        # return self.items.pop()
        current = self.items.head 
        data = current.data
        if current:
            self.items.head = current.get_next()
        
        return data
        
    def get_stack(self):
        return self.items.get_list()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.get_stack())
print(s.pop())
# print(s.get_stack())
print(s.pop())
# print(s.get_stack())
print(s.pop())
# print(s.get_stack())
print(s.pop())
# print(s.get_stack())
print(s.pop())
print(s.get_stack())