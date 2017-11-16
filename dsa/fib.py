""" 
                                || Fibonacci sequence || 
                                
f(n) = f(n - 1) + f(n - 2); n > 1
       n                  ; n = 0, 1 
"""

mem = {}

def fib(n):
    if n <= 1:
        return n
    elif mem[n] != -1:
        return mem[n]
    mem[n] = fib(n - 1) + fib(n - 2)
    return mem[n]

def main():
    n = int(input('n: '))
    for i in range(n+1):
        mem[i] = -1
    print(fib(n))

main()