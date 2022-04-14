while True:
    sign = input('Введите знак опериации (+, -, *, /) или 0 для завершения программы: ')
    if sign not in ('0', '+', '-', '/', '*'):
        sign = input('Введите знак из предложенных: +, -, *, /, 0 - ')
    elif sign == '0':
        print('Операция завершена')
        break
    else:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        while sign == '/' and num2 == 0:
            num2 = float(input('Невозможно деление на ноль, введите другое второе число: '))
        print(num2)
        if sign == '+':
            print(f'Операция сложения чисел {num1} {num2} и равна {num1+num2}')
        elif sign == '/':
            print(f'Операция деления чисел {num1} и {num2} равна {num1/num2}')
        elif sign == '*':
            print(f'Операция умножения чисел {num1} и {num2} равна {num1*num2}')
        else:
            print(f'Операция вычитания чисел {num1} и {num2} равна {num1-num2}')
