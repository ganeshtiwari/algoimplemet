medians = []
def selection(a_list, i):
    if len(a_list) // 5 > 0:
        medians.append(divide_list(a_list[: 5]))
    medians.