
def digits(n):
    while n > 0:
        yield n % 10
        n /= 10
s = 0
# too much but doesn't matter
for n in range(10, 7 * 9 ** 5):
    powsum = sum([d**5 for d in digits(n)])
    if powsum == n:
        s += n

print s