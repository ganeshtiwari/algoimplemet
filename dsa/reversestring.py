def reverse_string(a_str):
    if len(a_str) <= 1:
        return a_str
    else:
        return reverse_string(a_str[1: ]) + a_str[0]


# print(reverse_string('to the hose'))

def remove_space(a_str):
    a_str = list(a_str)
    while ' ' or "'" in a_str:
        try:
            a_str.pop(a_str.index(' '))
        except:
            a_str.pop(a_str.index("'"))
    
    return ''.join(a_str)


def is_palindrome(a_string):
    a_string = a_string.lower()
    a_string = remove_space(a_string)
    print(a_string)
    if a_string == reverse_string(a_string):
        return True
    else:
        return False

a_str = "Go hang a salami; I’m a lasagna hog"
print(is_palindrome(a_str))