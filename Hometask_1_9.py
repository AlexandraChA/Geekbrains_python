numbers = input('Введите список из трех чисел через пробел: ').split(' ') 
numbers = [float(i) for i in numbers]
num = None
for i in numbers:
    if i > min(numbers):
        if i < max(numbers):
            num = i
if num != None:
    print(f'Среднее число в списке {num}')
else:
    print('Невозможно найти среднее число в списке')    