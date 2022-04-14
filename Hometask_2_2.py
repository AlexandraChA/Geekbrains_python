num = input('Введите целое число: ')
while num.isdigit() == False:
    num = input('Ошибка ввода. Введите целое число: ')
num = int(num)
c1 = 0
c2 = 0
while num > 0:
    d = num % 10
    if d % 2 == 0:
        c1 += 1
    else:
        c2 +=1    
    num = num // 10   
print(f'Количество четных цифр в числе равно {c1}')
print(f'Количество нечетных цифр в числе равно {c2}')