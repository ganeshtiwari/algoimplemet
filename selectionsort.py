def selectionsort(a_list):
    count = 0
    for i in range(len(a_list)):
        pos_of_min = i
        for j in range(i, len(a_list)):
            if a_list[pos_of_min] > a_list[j]:
                pos_of_min = j
                count += 1
        a_list[pos_of_min], a_list[i] = a_list[i], a_list[pos_of_min]
    print(count)
    return a_list

a_list = [5, 4, 3, 2, 1, 0]

print(selectionsort(a_list))
