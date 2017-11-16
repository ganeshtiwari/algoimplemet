def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
                
    return a_list

a_list = [10, 2,3 , 5,7, 200, 0, 500, 1]
# print(bubble_sort(a_list))

def short_bubble_sort(a_list):
    exchanges = True
    count = 0
    pass_num = len(a_list) - 1
    while pass_num > 0 and  exchanges:
        for i in range(pass_num):
            exchanges = False
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                count += 1
        
        pass_num -= 1
    print(count, "comparisions")
    return a_list

print(short_bubble_sort(a_list))