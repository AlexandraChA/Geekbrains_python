from random import randint
n = int(input('Введите количество случайных чисел в массиве: '))
l = []
for i in range(n):
    l.append(randint(0,100))
l_max_ind = l.index(max(l)) 
l_min_ind = l.index(min(l)) 
print(f'В списке {l} наибольшее число стоит на {l_max_ind} месте (отсчет с нуля), а наименьшее - {l_min_ind}')
l[l_max_ind], l[l_min_ind] = l[l_min_ind], l[l_max_ind]
print(f'После того, как наибольшее число поменяли с наименьшим, список выглядит следующим образом: {l}')