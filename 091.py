
import numpy as np
from fractions import gcd

size = 50
result = 3*size**2 ## special cases
for a in range(1, size+1):
    for b in range(1, size+1):
        f = gcd(a, b)
        result += min(b*f / a, (size - a)*f / b) * 2

print result