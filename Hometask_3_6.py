l_num = input('Введите список чисел через пробел: ').split(' ')
for i in range(len(l_num)):
    l_num[i]= int(l_num[i])
max_ind = l_num.index(max(l_num))
min_ind = l_num.index(min(l_num))
if max_ind > min_ind:
    s = sum(l_num[(min_ind + 1):max_ind])
else:
    s = sum(l_num[(max_ind + 1):min_ind])  
if s != None:
    print(f'Максимальный и минимальный элементы массива {max(l_num)} и {min(l_num)}, их места в массиве {max_ind} и {min_ind} соотвественно. Сумма элементов между ними равна {s}')      
else:
    print('Между максимальным и минимальным элементами в списке нет других элементов')    