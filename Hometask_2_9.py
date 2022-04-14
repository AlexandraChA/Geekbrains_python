def right_input(a):
    while a.isdigit() == False or int(a) < 0:
            a = input('Ошибка ввода. Необходимо ввести натуральное число: ')
    return int(a)
num = input('Введите натуральное число или "стоп" для завершения списка чисел: ')
l = []
max_s = 0
max_n = 0
while num != 'стоп':
    num = right_input(num)  
    l.append(num)
    n = num
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_s:
        max_s = s
        max_n = num
    num = input('Введите следующее число: ')    
print(f'В последовательности {l} максимальная сумма цифр у числа {max_n}, сумма цифр равна {max_s}')      