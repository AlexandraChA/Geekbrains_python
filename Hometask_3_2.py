l_num = input('Введите список чисел через пробел: ').split(' ')
l_ind = []
for i in range(len(l_num)):
    l_num[i] = int(l_num[i])
    if l_num[i]%2==0:
        l_ind.append(i) 
print(f'Для массива чисел {l_num} четные числа стоят под следующими индексами: {l_ind} (отсчет с нуля)')