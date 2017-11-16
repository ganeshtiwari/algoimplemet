class Stack:
    def __init__(self, size):
        self.items = [None] * size
        self.top = -1
        self.size = size
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, item):
        self.top = self.top + 1
        if self.top >= self.size:
            print('StackOverflow')
            self.top = self.top - 1
            return 
        else:
            self.items[self.top] = item
            
    def pop(self):
        if not self.is_empty():
            top_item = self.items[self.top]
            self.top = self.top - 1
            return top_item
        else:
            print("StackUnderflow")
            return 
    

