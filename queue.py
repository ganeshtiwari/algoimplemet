class Queue:
    def __init__(self, size):
        self.items = [None] * size 
        self.head = 0
        self.tail = 0
        self.size = size 
    
    def enqueue(self, data):
        self.items[self.tail] = data
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail = self.tail + 1
    
    def dequeue(self):
        x = self.items[self.head]
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head = self.head + 1
        return x
