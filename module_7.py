def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(20, 28))
print(gcd(98, 56))