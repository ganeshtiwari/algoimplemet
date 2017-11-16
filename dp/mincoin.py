"""
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. 
Find the minimum number of coins the sum of which is S (we can use as many coins
of one type as we want), or report that it’s not possible to select coins in such
a way that they sum up to S.
"""
import sys


def mincoins(v, s):
    n = len(v)
    m = [sys.maxsize for i in range(s + 1)]
    m[0] = 0
    for i in range(1, s + 1):
        for j in range(n):
            if v[j] <= i and m[i-v[j]] + 1 < m[i]:
                m[i] = m[i-v[j]] + 1
    if sys.maxsize == m[s]:
        return ("Can't do it")
    else:
        return m[s]

print(mincoins([2, 5, 3], 1))