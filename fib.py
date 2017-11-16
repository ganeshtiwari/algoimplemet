def fib(n):
    memo = []
    for i in range(n+1):
        memo.append(-1)
    memo[0] = 0
    memo[1] = 1
    return calcFib(n, memo)

def calcFib(n, memo):
    if memo[n] != -1:
        return memo[n]
    memo[n] = calcFib(n-1, memo) + calcFib(n-2, memo)
    return memo[n]

print(fib(4))
