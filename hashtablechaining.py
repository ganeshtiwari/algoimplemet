import singlelinkedlist
from singlelinkedlist import SingleLinkedList


class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
        self.slots = [None] * self.size 
    
    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] == None:
            l = SingleLinkedList()
            self.slots[hash_value] = key
            self.data[hash_value] = data
            l.add(data)
        else:
            if self.slots[hash_value] == key:
                l.add(data)

    def hash_function(self, key, no_of_slots):
        return key % no_of_slots
    
    def search(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        pos = start_slot
        found = False 
        stop = False
        while self.slots[pos] != key and not found and not stop:
            if self.slots[pos] == key:
                current = l.head
                
                found = True
            else:
                if self.slots[pos] == start_slot:
                    stop = True
                
    def __setitem__(self, key, data):
        self.put(key, data)
    
    def __getitem_(self, key):
        return self.search(key)

h = HashTable(9)
h[1] = 1
h[2] = 2
h[1] = 5
