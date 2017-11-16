def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item <  a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


a_list = [10, 20, 30, 40]
# print(binary_search(a_list, 10))

def alter_binary_search(a_list, item):
    if len(a_list) == 0:
        return False
    midpoint = len(a_list) // 2
    if item == a_list[midpoint]:
        return True
    else:
        if item < a_list[midpoint]:
            a_list = a_list[: midpoint]
        else:
            a_list = a_list[midpoint + 1: ]
        return alter_binary_search(a_list, item)

item = 1 
print(alter_binary_search(a_list, item))