from collections import deque
from distutils.log import debug
d_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
d_16_rev = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}               
num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
sign = input('Введите знак сложения или умножения: ')
result = deque()
def nums_16(a, b, sign):
    addit = 0
    if sign == '+':
        if len(b) > len(a):
            a, b = deque(b), deque(a)
        else:
            a, b = deque(a), deque(b)    
        while a:
            if b:
                s = d_16[a.pop()] + d_16[b.pop()] + addit    
            else:
                s = d_16[a.pop()] + addit 
            addit = 0    
            if s < 16:
                result.appendleft(d_16_rev[s])
            else:
                addit = 1   
                result.appendleft(d_16_rev[s-16]) 
        if addit != 0:
            result.appendleft('1')    
        return result
    if sign == '*':
        p = deque([deque() for _ in range(len(b))])
        b = deque(b)
        for i in range(len(b)):
            q = d_16[b.pop()]
            for j in range(len(a)-1, -1, -1):
                p[i].appendleft(q*d_16[a[j]])
            for z in range(i):
                p[i].append(0)
        addit = 0
        for e in range(len(p[-1])):
            s = addit
            for i in range(len(p)):
                if p[i]:
                    s += p[i].pop()
            if s < 16:
                result.appendleft(d_16_rev[s])
            else:
                result.appendleft(d_16_rev[s % 16])  
                addit = s // 16
        if addit != 0:  
            result.appendleft(d_16_rev[addit])  
        return result               
    else:
        print('Необохдимо ввести знак сложения или умножения.')        
print("".join(nums_16(num1, num2, sign)))        