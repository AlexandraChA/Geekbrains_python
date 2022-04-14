from random import randint
def right_input(a):
    while a.isdigit() == False or int(a) < 0 or int(a) > 100:
            a = input('Ошибка ввода. Необходимо ввести целое число от 0 до 100: ')
    return a
c = 0
num = randint(0, 100)
print(num)
while c != 10:
    if c == 0:
        g = input('Угадайте число от 0 до 100: ')
        g = int(right_input(g))
    if g == num:
        print(f'Поздравляем, Вы угадали число! Количество попыток {c+1}')
        break
    elif g > num:
        g = input('Загаданное число меньше, попробуйте еще: ')
        g = int(right_input(g))
    else:
        g = input('Загаданное число больше, попробуйте еще: ')
        g = int(right_input(g))      
    c += 1
    if c == 10:
        print(f'Вы проиграли, 10 попыток закончились. Загаданное число {num}')