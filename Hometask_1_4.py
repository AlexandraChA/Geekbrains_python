from random import randint, uniform

t = input('Выберите целые числа (ц), вещественные числа (в) или символы (с): ')
l1 = input('Введите первую границу: ')
l2 = input('Введите вторую границу: ')
if t == 'ц':
    print(f'Рандомное целое число в указанных границах - {randint(int(l1), int(l2))}')
elif t == 'в':
    print(f'Рандомное вещественное число в указанных границах - {uniform(float(l1), float(l2))}')
elif t == 'с':
    print(f'Рандомная буква между указанными - {chr(randint(ord(l1), ord(l2)))}')
else:
    print('Выберите тип данных из списка')        