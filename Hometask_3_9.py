n_line = int(input('Введите количество строк: '))
n_column = int(input('Введите количество столбцов: '))
l = []
l_2 = []
for i in range(n_line):
    for j in range(n_column):
        num = int(input('Введите число (неотрицательное): '))
        l_2.append(num)
    l.append(l_2)  
    l_2 = []  
for i in l:
    print(i)
max_num = -1
max_lim = 100
for j in range(n_column):
    for i in range(n_line):
        if l[i][j] < max_lim:
            max_lim = l[i][j]
    if max_lim > max_num:
        max_num = max_lim 
print(f'В указанной матрице максимальное число из минимальных чисел в каждом столбце равно {max_num}')           