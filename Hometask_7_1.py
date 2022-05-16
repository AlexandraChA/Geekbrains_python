from random import randint
s = []
for i in range(randint(1,50)):
    s.append(randint(-100,100))
print(s)
def bubble(l):
    swapped = False
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return l
print(bubble(s))       