from statistics import mean
num_ent = input('Введите количество предприятий: ')
while num_ent.isdigit() == False or int(num_ent) <= 0:
    num_ent = input('Количество предприятий должно быть целым числом, больше нуля. Введите еще раз: ')
num_ent = int(num_ent)
d = {}
avg_o = 0
for i in range(num_ent):
    name = input('Введите наименование предпрития: ')
    profits = input('Введите прибыль за 4 квартала через пробел: ').split(' ')
    profits = [int(i) for i in profits]
    avg = mean(profits)
    avg_o += avg
    d[name] = [profits, avg]
avg_o /= num_ent 
for i in d.keys():
    if d[i][1] > avg_o:
        print(f'Компания "{i}" имела за год прибыль выше среднего значения по всем придприятиям')
    elif d[i][1] < avg_o:
        print(f'Компания "{i}" имела за год прибыль ниже среднего значения по всем придприятиям')
    else:
        print(f'Компания "{i}" имела за год прибыль такую же как и среднее значение по всем придприятиям')  