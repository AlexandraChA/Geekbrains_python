l_num = input('Введите список чисел через пробел: ').split(' ')
max_freq = 0
freq_num = 0
for i in range(len(l_num)):
    l_num[i]= int(l_num[i])
    freq = l_num.count(l_num[i])
    if freq > max_freq:
        max_freq = freq
        freq_num = l_num[i]
print(f'В данном списке число {freq_num} встречается чаще всего, {max_freq} раз(a)')        