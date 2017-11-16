def minmax(a_list):
    minimum = a_list[0]
    maximum = a_list[1]
    if minimum > maximum:
        minimum, maximum = maximum, minimum
    for i in range(2, len(a_list)):
        if minimum > a_list[i]:
            print("If")
            minimum = a_list[i]
        elif maximum < a_list[i]:
            print("elif")
            maximum = a_list[i]
    return minimum, maximum

minimum, maximum = minmax([1, 2, 3, 4,5 ,6 ,7, 8])
print(minimum, maximum)