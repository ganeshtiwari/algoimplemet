def euclid_gcd(a, b):
    if a >= b:
        dividend = a
        divisor = b
    else:
        dividend = b
        divisor = a
    while divisor != 0:
        rem = dividend % divisor
        dividend = divisor
        divisor = rem
    
    return dividend

print(euclid_gcd(105, 350))