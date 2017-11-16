import stack 
from stack import Stack 

def infix_to_postfix(infix_expr):
    prec = {}
    prec['^'] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()
    # print(token_list)

    for token in token_list:
        # if token == '':
        #     continue
        # print(prec)
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            # print(op_stack.show())
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                # print(prec)
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return ''.join(postfix_list)


print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))

