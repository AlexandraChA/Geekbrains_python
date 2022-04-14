num = input('Введите любое натуральное число: ')
while num.isdigit() == False or int(num) < 0:
    num = input('Ошибка ввода. Введите натуральное число: ')
num = int(num)    
c1 = 0
c2 = num*(num+1)/2
while num > 0:
    c1 += num
    num -= 1
if c1 == c2:
    print(f'Равенство выполнено: {c1}={c2}') 
else:
    print(f'Равенство не выполнено: {c1}!={c2}')            