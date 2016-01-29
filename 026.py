### Reciprocal cycles
# https://projecteuler.net/problem=26


def division(n, d):
    """
    A cycle is defined by the number being divided and the divisor. Such a pair uniquely defines
    the sequence of numbers occurring as a result of the division - if such a pair occurs twice consequently,
    then the numbers between the occurrences are the elements of the cycle.
    """
    signatures = {}
    i = 0
    while True:
        if n == 0:
            break
        while n < d:
            n *= 10
        if n in signatures:
            cycle_len = i - signatures[n]
            return cycle_len
        else:
            signatures[n] = i
        n = n % d
        i += 1
    return 0

max_num = 0.
max_cycle = 0.

for i in range(3, 999, 2):
    cycle = division(1, i)
    if cycle > max_cycle:
        max_num = i
        max_cycle = cycle

print max_num, max_cycle
