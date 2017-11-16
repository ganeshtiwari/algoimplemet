"""
A table composed of N x M cells, each having a certain quantity of apples, 
is given. You start from the upper-left corner. At each step you can go down 
or right one cell. Find the maximum number of apples you can collect.
"""

def maxapples(m, row, col):
    s = [[0 for i in range(row)] for j in range(col)]
    for 
    for i in range(row):
        for j in range(col):
            s[i][j] = m[i][j] + max(s[i][j-1], s[i-1][j])
