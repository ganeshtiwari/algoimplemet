class DArrayHeap:
    def __init__(self, d):
        self.heap_list = [0]
        self.heap_size = 0
        self.no_of_child = d
    
    def heapify(self, i):
        count = 0
        d = self.no_of_child
        pos_of_child = d * i - (d - 2)
        pos_of_max = i
        # print(self.heap_list[1: ])
        while  count < d:
            # print('pos_of_child: ', pos_of_child)
            temp = pos_of_max
            if pos_of_child <= self.heap_size and self.heap_list[pos_of_max] < self.heap_list[pos_of_child]:
                pos_of_max = pos_of_child
            count += 1
            pos_of_child = pos_of_child + 1 #Fuck this shit(idiot bug)
            # if pos_of_max == temp:
            #     break
        if pos_of_max != i:
            self.heap_list[i], self.heap_list[pos_of_max] = self.heap_list[pos_of_max], self.heap_list[i]
            self.heapify(pos_of_max)
    
    def build_heap(self, a_list):
        n = len(a_list)
        self.heap_list = [0] + a_list
        self.heap_size = n
        for i in range(n // self.no_of_child + 1, 0, -1):
            # print(i)
            self.heapify(i)
        
    def extract_max(self):
        maximum = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_list.pop()
        self.heapify(1)
    
    def insert(self, key):
        self.heap_list.append(key)
        self.heap_size = self.heap_size + 1
        self.heap_up(self.heap_size)

    def heap_up(self, i):
        l

    def __str__(self):
        return str(self.heap_list[1: ])

m = DArrayHeap(3)
m.build_heap([1, 2, 3, 4, 5, 6, 7, 8])
print(m)
m.extract_max()
print(m)
m.insert(8)
print(m)