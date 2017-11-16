# adding two binary numbers
def addbin(a, b, n):
    '''
    a: List of binary bits
    b: List of binary bits
    n: number of bits in a and b
    '''
    carry = 0
    i = n - 1
    c = []
    while i >= 0:
        ans = carry + a[i] + b[i]
        if ans > 1:
            carry = 1
            if ans == 2:
                ans = 0
            else:
                ans = 1
        c.append(ans)
        i -= 1
    c.append(carry)
    c.reverse()
    return c

print(addbin([1, 0, 1, 0], [1, 1, 1, 1], 4))

        