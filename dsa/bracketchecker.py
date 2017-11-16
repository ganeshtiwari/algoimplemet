import stack
from stack import Stack

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in  '({[':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False

print(par_checker('((((())))'))
                    balanced = False
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open, close):
    opens = '({['
    closes = ')}]'
    return opens.index(open) == closes.index(close)


print(par_checker('(((([}]))))'))