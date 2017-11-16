import singlelinkedlist
from singlelinkedlist import SingleLinkedList

class Queue:
    def __init__(self):
        self.items = SingleLinkedList()
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.add(item)
    
    def dequeue(self):
        if not self.is_empty():
            data = self.items.tail.data
            self.items.tail.set_next(None)
            return data
    
    def get_queue(self):
        return self.items.get_list()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.get_queue())
q.dequeue()
print(q.get_queue())
q.dequeue()
print(q.get_queue())
q.dequeue()
print(q.get_queue())
