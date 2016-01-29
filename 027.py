from itertools import count, islice
from math import sqrt

# brute-force

def isPrime(n):
    if n < 2: return False
    return all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

def f(a, b, n): return n**2 + a*n + b

maxN = 0
maxa = 0
maxb = 0
for a in range(-999, 1000, 1):
    for b in range(-999, 1000, 1):
        n = 0
        while isPrime(f(a, b, n)):
            n += 1
        if n > maxN:
            maxN = n
            maxa = a
            maxb = b

print maxa * maxb, maxa, maxb
