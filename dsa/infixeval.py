import stack
from stack import Stack 

def infix_eval(infix_expr):
    oper_stack = Stack()
    op_stack = Stack()
    token_list = infix_expr.split()
    # print(token_list)
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['-'] = 2
    prec['+'] = 2
    prec['('] = 1

    for token in token_list:
        # print(token)
        if token in '0123456789':
            op_stack.push(int(token))
        
        elif token in '/*-+':
            if (not oper_stack.is_empty()) and (prec[oper_stack.peek()] >= prec[token]):
                operator = oper_stack.pop()
                op_stack.push(do_math(operator, op_stack))
            oper_stack.push(token)
        elif token =='(':
            oper_stack.push(token)
        elif token == ')':
            top_oper = oper_stack.pop()
            while top_oper != '(':
                operator = top_oper
                top_oper = oper_stack.pop()
                op_stack.push(do_math(operator, op_stack))
        print(op_stack.show())
        print(oper_stack.show())  
    if not op_stack.is_empty():
        op_stack.push(do_math(oper_stack.pop(), op_stack))

    return op_stack.pop()

def do_math(operator, op_stack):
    second_op = op_stack.pop()
    first_op = op_stack.pop()

    if operator == '-':
        return first_op -  second_op
    elif operator == '+':
        return first_op + second_op
    elif operator == '*':
        return first_op * second_op
    elif operator == '/':
        return first_op / second_op
    elif operator == '^':
        return first_op ^ second_op

print(infix_eval("2 + ( 6 * 6 - 5 - ( 3 - 2 ) )"))