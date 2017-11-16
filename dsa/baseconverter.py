import stack 
from stack import Stack 

def base_converter(num, base):
    digits = '0123456789ABCDEF'
    rem_stack = Stack()
    
    while num > 0:
        rem_stack.push(digits[num % base])
        num = num // base

    new_string = ''
    while not rem_stack.is_empty():
        new_string += str(rem_stack.pop())
    
    return new_string

print(base_converter(204, 16))