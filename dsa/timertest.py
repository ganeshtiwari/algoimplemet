def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = [range(1000)]

def test5():
    ls = [1, 2, 3, 4, 5, 6, 7, 6, 6, 6, 6,6 ,6 ,6 , 6,6 ,6 ,6 ,6 ]
    ls.pop()

def test6():
    ls = [1, 2, 3, 4, 5]
    ls.pop(3)

def test7():
    ls = [1, 2, 3, 4, 5]
    ls.pop(1)

import timeit
from timeit import Timer

# t1 = Timer("test1()", "from __main__ import test1")
# t2 = Timer("test2()", "from __main__ import test2")
# t3 = Timer("test3()", "from __main__ import test3")
# t4 = Timer("test4()", "from __main__ import test4")
t5 = Timer("test5()", "from __main__ import test5")
t6 = Timer("test6()", "from __main__ import test6")
t6 = Timer("test7()", "from __main__ import test7")

# print("concat ",t1.timeit(number=100), "milliseconds")
# print("append ",t2.timeit(number=100), "milliseconds")
# print("comp ",t3.timeit(number=100), "milliseconds")
# print("range ",t4.timeit(number=100), "milliseconds")
print("lastpop ",t5.timeit(number=100), "milliseconds")
print("middlepop ",t5.timeit(number=100), "milliseconds")
print("firstpop ",t5.timeit(number=100), "milliseconds")

