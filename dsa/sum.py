def sum_of_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = 2
sum = sum_of_n(n)
print(sum)