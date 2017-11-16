def insertion_sort(a_list):
    count = 0
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            count += 1

        a_list[position] = current_value

    print(count, "comparisions")
    return a_list

a_list = [10, 2,3 , 5,7, 200, 0, 500, 1]
print(insertion_sort(a_list))