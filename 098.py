__author__ = 'tutekma'

import collections
import itertools
import math

# https://projecteuler.net/problem=98
def hash(s):
    return collections.Counter(s)

def sq(s1, s2):
    max = 0

    #chars
    m = hash(s1)
    n = len(m)
    digits = range(0, 10)

    for subset in itertools.permutations(digits, n):
        n1 = s1
        n2 = s2
        #false if mapping results in leading zero
        conv = True
        for c, n in zip(m.keys(), subset):
            #leading zero
            if s1[0] == c and n == 0 or s2[0] == c and n == 0:
                conv = False
                break
            n1 = n1.replace(c, str(n))
            n2 = n2.replace(c, str(n))
        if not conv:
            continue
        num1 = int(n1)
        num2 = int(n2)

        if math.sqrt(num1).is_integer() and math.sqrt(num2).is_integer():
            if (num1 > max):
                max = num1
            if (num2 > max):
                max = num2
    return max


f = open('./data/p098_words.txt', 'r')
words = [item.strip('\"') for item in f.readline().split(',')]

max = 0
for word1 in words:
    for word2 in words:
        if word1 == word2:
            continue
        if not hash(word1) == hash(word2):
            continue
        s = sq(word1,word2)
        if s > max:
            max = s

print(max)
# ?