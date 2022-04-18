l_num = input('Введите список чисел через пробел: ').split(' ')
for i in range(len(l_num)):
    l_num[i]= int(l_num[i])
l_num_res = l_num.copy()   
min_num1 = min(l_num)
l_num.remove(min_num1)
min_num2 = min(l_num)
print(f'В списке {l_num_res} наименьший элемент - {min_num1}, следующий наименьший - {min_num2}')