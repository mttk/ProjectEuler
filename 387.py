
from math import sqrt
from itertools import count, islice

# strong, right truncatable Harshad prime numbers who don't need no man

def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    # print(r)
    return r


def check_harshad(n):
    return n % sum_digits(n) == 0


def isPrime(n):
    if n < 2: return False
    return all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def condition(n):
    if not isPrime(n):
        return False
    _n = n // 10
    if not check_harshad(_n):
        return False
    _n = _n / sum_digits(_n)
    #print(_n)
    if not isPrime(_n):
        return False
    return True

# first generate all right truncatable harshad numbers
candidates = []
harshads = []
# initialize candidates
# all one digit numbers are harshad numbers
# but not strong!

for d in range(1, 10):
    candidates.append(d)

# print(candidates)
# loop over digits (< 10^14)
for i in range(13):
    print(i)
    new_candidates = []
    for n in candidates:
        for d in range(0, 10):
            candidate = n * 10 + d
            if check_harshad(candidate):
                new_candidates.append(candidate)
            if candidate % 2 == 1:
                harshads.append(candidate)
    candidates = new_candidates
    print(len(candidates))

print(len(harshads))
harshad_sum = 0
for harshad in harshads:
    if condition(harshad):
        harshad_sum += harshad
# 696067597313468
print(harshad_sum)
