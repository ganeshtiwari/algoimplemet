class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0
    
    def heapify(self, i): # Maintains min_heap property ie heap[i] <= heap[i * 2] and heap[i * 2 + 1]
        l = i * 2
        r = i * 2 + 1
        if l <= self.heap_size and self.heap_list[i] > \
             self.heap_list[l]:
            pos_of_small = l 
        else:
            pos_of_small = i
        if r <= self.heap_size and self.heap_list[pos_of_small] > \
             self.heap_list[r]:
            pos_of_small = r
        if pos_of_small != i:
            self.heap_list[pos_of_small], self.heap_list[i] = \
                self.heap_list[i], self.heap_list[pos_of_small]
            self.heapify(pos_of_small)
    
    def build_heap(self, a_list):
        n = len(a_list)
        self.heap_size = n
        self.heap_list = [0] + a_list
        for i in range(n // 2, 0, -1):
            print(i)
            self.heapify(i)
    
    def heap_min(self):
        return self.heap_list[1]
    
    def heap_extract_min(self):
        minimum = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.heap_list.pop()
        self.heapify(1)
    
    def heap_decrease_key(self, i, key):
        if key > self.heap_list[i]:
            print("Key is expected to e smaller than this")
        else:
            self.heap_list[i] = key
            self.heapify(i) 
    
    def heap_insert(self, key):
        self.heap_list.append(key)
        self.heap_size = self.heap_size + 1
        self.heap_up(self.heap_size)

    def heap_up(self, i):
        while i > 1 and self.heap_list[i//2] > self.heap_list[i]:
            self.heap_list[i//2], self.heap_list[i] = \
                    self.heap_list[i], self.heap_list[i//2]
            i = i // 2

    def heap_merger(self, a_list):
        self.build_heap(a_list)
        # print(self.heap_list)
        b_list = []
        while self.heap_size > 0:
            temp_list = self.heap_min()
            # print(temp_list)
            self.heap_extract_min()
            for num in temp_list:
                b_list.append(num)

        return b_list

    def __str__(self):
        return str(self.heap_list[1:  ])
    

m = MinHeap()
m.build_heap([1, 2, 3, 4, 5, 6, 7, 8])
# print(m)
# print(m.heap_min())
# m.heap_insert(5)
print(m)
