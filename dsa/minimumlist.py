def first_way(ls):
    minimum = ls[0]
    for i in range(len(ls) - 1):
        for j in range(i + 1, len(ls)):
            # print(ls[j])
            if minimum > ls[j]:
                minimum = ls[j]
    return minimum

ls = [2, 3, 4, 0,  5, 6, 7, 1]
print(first_way(ls))

def second_way(ls):
    minimum = ls[0]
    for i in range(1, len(ls) -1 ):
        if minimum > ls[i]:
            minimum = ls[i]
    return minimum
print(second_way(ls))
