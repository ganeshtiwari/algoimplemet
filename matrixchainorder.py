import sys

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]
    # print(m)
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            # print('i: ', i, 'j: ', j)
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    # print(m)
    # print(s)
    # return m[0][n - 1]
    print_optimal_parens(s, 0, n-1)

def print_optimal_parens(s, i, j):
    if i == j:
        print('A', end='')
        print(i, end='')
    else:
        print("(", end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end='')


print(matrix_chain_order([2, 3, 6, 4, 5]))