def main():
    t = [[0],
        [0, 2, 3, 1, 3, 4],
        [0, 2, 1, 2, 2, 1]
        ]
    e1 = 2
    e2 = 4
    x1 = 3
    x2 = 2
    a = [[0],
        [0, 7, 9, 3, 4, 8, 4],
        [0, 8, 5, 6, 4, 5, 7]
        ]
    fastest_way(e1, e2, a, t, x1, x2)

def fastest_way(e1, e2, a, t, x1, x2):
    n = 6
    f1 = [0]
    f1.append(e1 + a[1][1])
    f2 = [0]
    f2.append(e2 + a[2][1])
    l = [[0],
        [0, 0],
        [0, 0]
        ]
    for j in range(2, n+1):
        if f1[j-1] + a[1][j] <= f2[j-1] + t[2][j-1] + a[1][j]:
            f1.append(f1[j-1] + a[1][j])
            l[1].append(1)
        else:
            f1.append(f2[j-1] + t[2][j-1] + a[1][j])
            l[1].append(2)
        if f2[j-1] + a[2][j] <= f1[j-1] + t[1][j-1] + a[2][j]:
            f2.append(f2[j-1] + a[2][j])
            l[2].append(2)
        else:
            f2.append(f1[j-1] + t[1][j-1] + a[2][j])
            l[2].append(1)
    if f1[n] + x1 <= f2[n] + x2:
        f = f1[n] + x1
        l[0][0] = 1
    else:
        f = f2[n] + x2
        l[0][0] = 2
    # print(f)
    # print(f1)
    # print(f2)
    # print(l1)
    # print(l2)
    print_line(l, n)

def print_line(l,  n):
    i = l[0][0] 
    print("line", i, " station", n)
    for j in range(n, 1, -1):
        i = l[i][j]
        print("line", i, " station", j - 1)

main()