class MaxHeap:
    def __init__(self):
        self.heap_size = 0
        self.heap_list = [0]
    
    def heapify(self, i):
        l = i * 2
        r = i * 2 + 1
        # print(self.heap_list[1: ])
        # print(self.heap_size)
        # print(self.heap_size)
        if l <= self.heap_size and self.heap_list[i] < self.heap_list[l]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.heap_list[largest] < self.heap_list[r]:
            largest = r
        if largest != i:
            self.heap_list[i], self.heap_list[largest] = \
                self.heap_list[largest], self.heap_list[i]
            self.heapify(largest)
    
    def build_heap(self, a_list):
        self.heap_list = [0] + a_list
        n = len(a_list)
        self.heap_size = n 
        for i in range(n // 2, 0, -1):
            self.heapify(i)
    
    def heap_sort(self, a_list):
        self.build_heap(a_list)
        for i in range(len(a_list), 1, -1):
            self.heap_list[1], self.heap_list[i] = \
                self.heap_list[i], self.heap_list[1]
            self.heap_size = self.heap_size - 1
            self.heapify(1)

    def extract_max(self):
        maximum = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.heap_list.pop()
        self.heapify(1)

    def heap_increase_key(self, i, key):
        if key < self.heap_list[i]:
            raise KeyError('Key smaller than current key')
        self.heap_list[i] = key
        self.heap_up(i)
    
    def heap_up(self, i):
        while i > 1 and self.heap_list[i] > self.heap_list[i // 2]:
            self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def heap_insert(self, key):
        self.heap_list.append(key)
        self.heap_size = self.heap_size + 1
        self.heap_up(self.heap_size)

    def heap_delete(self, i):
        self.heap_list[i] = self.heap_list[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.heap_list.pop()
        self.heapify(i)

    def __str__(self):
        return str(self.heap_list[1: ])

m = MaxHeap()
m.build_heap([1, 2, 3, 4, 5, 6, 7, 8])
# print(m)
# m.extract_max()
# print(m)
# m.heap_insert(1)
# m.heap_insert(2)
# m.heap_insert(3)
# m.heap_insert(4)
# m.heap_insert(5)
# print(m)
# m.heap_delete(1)
# m.heap_delete(3)
