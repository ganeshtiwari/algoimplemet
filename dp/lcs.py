"""Need to Work More # Incorrect """

def lcs(a, b):
    l1 = len(a) - 1
    l2 = len(b) - 1
    m = [[0 for i in range(l1 + 2)] for j in range(l2 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            print('i: ', i, 'j: ', j)
            print(m)
            if a[i] == b[j]:
                m[i][j] = m[i-1][j-1] + 1
            else:
                m[i][j] = max(m[i-1][j], m[i][j-1])
    print(m)

A = [0, 'a', 'b', 'c', 'd', 'a', 'f']
B = [0, 'a', 'c', 'b', 'c', 'f']
lcs(A, B)