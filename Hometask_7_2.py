import imp
from random import random, randint
import math
s = []
for i in range(randint(1,10)):
    s.append(round((random()*50),2))
print(s)
def merge(l):
    n = len(l)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = l[i]
            j = i 
            while l[j - interval] > temp and j >= interval:
                l[j] = l[j - interval]
                j -= interval
            l[j] = temp
        k -= 1
        interval = 2**k - 1
    return l
print(merge(s))        