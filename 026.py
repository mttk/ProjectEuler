### Reciprocal cycles
# https://projecteuler.net/problem=26

def division(n, d):
    signatures = {}
    i = 0
    while True:
        if n == 0:
            break
        while n < d:
            n*=10
        div = n // d
        mod = n % d
        if (div, mod) in signatures:
            cycle_len = i - signatures[(div, mod)]
            return cycle_len
        else:
            signatures[(div, mod)] = i
        n = mod
        i += 1

max_num = 0.
max_cycle = 0.

for i in range(3, 999, 2):
    cycle = division(1, i)
    if cycle > max_cycle:
        max_num = i
        max_cycle = cycle

print max_num, max_cycle
