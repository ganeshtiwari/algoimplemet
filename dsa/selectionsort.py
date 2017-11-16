def selection_sort(a_list):
    count = 0
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location 
                count += 1
        
        a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]
    print(count, "comparisions")
    return a_list


a_list = [5, 4, 3, 2, 1, 0]
print(selection_sort(a_list))