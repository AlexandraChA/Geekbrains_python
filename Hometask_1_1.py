num = int(input('Введите трехзначное число: '))
if 100 <= num < 1000:
    n1 = num // 100
    n2 = (num % 100) // 10
    n3 = num % 10
    print(f'Сумма трех цифр равна {n1+n2+n3}')
    print(f'Произведение трех цифр равно {n1*n2*n3}')
else:
    print('Необходимо ввести трехзначное число')