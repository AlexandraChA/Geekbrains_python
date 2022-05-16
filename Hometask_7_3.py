from random import randint
m = randint(1,5)
s=[]
for i in range(2*m+1):
    s.append(randint(0,20))
print(s)    
def get_meadian(l):
    med = 0
    for i in range(len(l)):
        less = []
        more = []
        for j in range(len(l)):
            if i != j:
                if l[j]<l[i]:
                    less.append(l[j])
                else:
                    more.append(l[j])
                # print(l[i], less, more)
            if len(less) == len(more):
                med = l[i]
    return med
print(get_meadian(s))