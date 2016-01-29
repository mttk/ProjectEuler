# summmmmmmm
sum = 1
n = 1

dims = 1001 + 1

for nd in xrange(3, dims, 2):
    increment = nd - 1
    print increment

    for _ in range(4):
        n += increment
        sum += n

print sum
