import dequeue
from dequeue import Dequeue


def palindrome_checker(a_string):
    char_dequeue = Dequeue()
    for ch in a_string:
        char_dequeue.add_rear(ch)
        
    still_equal = True
    
    while char_dequeue.size() > 1 and still_equal:
        first = char_dequeue.remove_rear()
        last = char_dequeue.remove_front()
        if first == last:
            still_equal = True
        else:
            still_equal = False
        
    return still_equal

print(palindrome_checker('aba aba'))