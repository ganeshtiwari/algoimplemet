import stack 
import binarytree
import operator 

from stack import Stack 
from binarytree import BinaryTree


def build_parse_tree(fp_exp):
    if " " not in fp_exp:
        fp_list = []
        temp = ''
        i = 0
        while i < len(fp_exp):
            while fp_exp[i] in '0123456789':
                temp = temp + fp_exp[i]
                i += 1
            if temp != '':
                fp_list.append(temp)
                temp = ''
            else:
                fp_list.append(fp_exp[i])
                i += 1
    else:
        fp_list = fp_exp.split()
        
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent 
        elif i in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    
    return e_tree

def evaluate(parse_tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, 
        '/': operator.truediv}
    
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left, evaluate(rigth)))
    else:
        return parse_tree.get_root_val()
    

def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

def print_expr(tree):
    str_val = ""
    if tree:
        str_val = '(' + print_expr(tree.get_left_child())
        str_val = str_val + tree.get_root_val()
        str_val = str_val + tree.get_right_child() + ')'

    return str_val
    

pt = build_parse_tree("((10+5)*3)")
print(pt.get_root_val())
            