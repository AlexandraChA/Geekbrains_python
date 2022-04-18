l_num = input('Введите список чисел через пробел: ').split(' ')
l_neg = []
l_ind = []
for i in range(len(l_num)):
    l_num[i]= int(l_num[i])
    if l_num[i] < 0:
        l_neg.append(l_num[i])
        l_ind.append(i) 
if l_neg != [] :
    print(f'Максимальное отрицательное число в списке равно {max(l_neg)} и стоит на {l_ind[l_neg.index(max(l_neg))]} месте (отсчет с нуля)')
else:
    print('В списке нет отрицательных чисел')    