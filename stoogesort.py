def stooge_sort(a_list):
    stooge_sort_helper(a_list, 0, len(a_list) - 1)

def stooge_sort_helper(a_list, first, last):
    if a_list[first] > a_list[last]:
        a_list[first], a_list[last] = a_list[last], a_list[first]
    if first + 1 >= last:
        return
    k = (last - first + 1) // 3 # Round down 
    stooge_sort_helper(a_list, first, last - k) # First two-third
    stooge_sort_helper(a_list, first + k, last) # Last two-third
    stooge_sort_helper(a_list, first, last - k) # First two-third again 

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
stooge_sort(a_list)
print(a_list)