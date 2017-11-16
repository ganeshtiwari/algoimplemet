import random


def randomized_select(a_list, pos_of_num):
    return(randomized_select_helper(a_list, 0, len(a_list) - 1, pos_of_num))

def randomized_select_helper(a_list, first, last, pos_of_num):
    if first == last:
        return a_list[first]
    elif first > last:
        return
    split_point = randomized_partition(a_list, first, last)
    no_of_elements = split_point - first + 1
    if pos_of_num == no_of_elements: # The pivot value is the answer
        return a_list[split_point]
    elif pos_of_num < no_of_elements:
        return randomized_select_helper(a_list, first, split_point - 1, pos_of_num)
    else:
        return randomized_select_helper(a_list, split_point + 1, last, pos_of_num - no_of_elements)

def randomized_partition(a_list, first, last):
    random_pos = random.randrange(first, last)
    a_list[random_pos], a_list[first] = a_list[first], a_list[random_pos]
    return partition(a_list, first, last)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last 
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1
        
        while right_mark >= left_mark and a_list[right_mark] >= pivot_value:
            right_mark -= 1
        
        if left_mark > right_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp 
    
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp 

    return right_mark


a_list = [1]
print(randomized_select(a_list, 5))
