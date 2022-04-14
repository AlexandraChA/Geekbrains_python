num = input('Введите целое число: ')
while num.isdigit() == False:
    num = input('Ошибка ввода. Введите целое число: ')
num = int(num)
l = []
while num > 0:
    d = num % 10
    l.append(d)
    num = num // 10  
l = [str(i) for i in l]
print("".join(l))