s = 0
l = []
l_2 = []
for i in range(4):
    for j in range(5):
        if j != 4:
            num = int(input('Введите число: '))
            l_2.append(num)
            s += num
        else:
            l_2.append(s)
            l.append(l_2)
            s = 0
            l_2 = []
for i in l:
    print(i)