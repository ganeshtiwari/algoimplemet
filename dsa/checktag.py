import stack 
from stack import Stack 


def html_tag_checker(tag_list):
    tag_stack = Stack()
    open_tag_list = ['<html>', '<head>', '<title>', '<div>', '<body>']
    close_tag_list = ['</html>', '</head>', '</title>', '</div>', '</body>']
    for tag in tag_list:
        if tag in open_tag_list:
            tag_stack.push(tag)
        
        elif tag in close_tag_list:
            if  not tag_stack.is_empty():
                tag_stack.pop()
            else:
                raise TagError


html_tag_checker(['<html>', '<head>', '<title>', '<div>', '<body>', '</html>', '</head>', '</title>', '</div>', '</body>'])