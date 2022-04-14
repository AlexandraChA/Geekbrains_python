def right_input(a):
    while a.isdigit() == False or int(a) < 0:
            a = input('Ошибка ввода. Необходимо ввести целое число: ')
    return a
num = input('Введите количество цифр в последовательности: ')
num = int(right_input(num))
d = input('Введите цифру для поиска по последовательности: ')
d = int(right_input(d))
l = []
c = 0
for i in range(num):
    ni = input('Введите число: ')
    ni = int(right_input(ni))
    l.append(ni)
    if ni == d:
        c += 1
print(f'В заданном списке {l} число {d} присутствует {c} раз(а).')
