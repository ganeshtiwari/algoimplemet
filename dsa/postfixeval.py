import stack 
from stack import Stack 

def postfix_eval(postfix_expr):
    op_stack = Stack()
    token_list = postfix_expr.split()
    
    for token in token_list:
        if token in '1234567890':
            op_stack.push(int(token))
        elif token in '/+-*':
            second_op = op_stack.pop()
            first_op = op_stack.pop()
            result = do_math(token, first_op, second_op)
            op_stack.push(result)
    return op_stack.pop()

def do_math(op, first_op, second_op):
    if op == '+':
        return first_op + second_op
    elif op == '-':
        return first_op - second_op
    elif op == '*':
        return first_op * second_op
    elif op == '/':
        return first_op / second_op
    else:
        raise FuckError
print(postfix_eval('7 8 + 3 2 + /'))