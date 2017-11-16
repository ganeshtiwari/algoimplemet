convert_str = '0123456789ABCDEF'
def to_str1(n, base):
    # print(n)
    if n < base:
        return n
    else:
        return str(to_str1(n // base, base)) + convert_str[n % base]

print(to_str1(200, 2))

import stack
from stack import Stack


r_stack = Stack()

def to_str2(n, base):
    while n > 0:
        if n < base:
            r_stack.push(convert_str[n])
        else:
            r_stack.push(n % base)
        n = n // base
    result = ''
    while not r_stack.is_empty():
        result = result + str(r_stack.pop())
    return result

print(to_str2(200, 2))
