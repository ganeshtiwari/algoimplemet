class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items
