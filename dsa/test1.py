def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib1(n):
    if n <= 1:
        return n
    else:
        f1 = 0
        f2 = 1
        for i in range(2, n+1):
            f = f1 + f2
            f1 = f2
            f2 = f
        return f

print(fib1(40))