import timeit
def sum_range(n):
    num = int(n)    
    l = [1]
    while num > 1:
        d = l[len(l)-1]/(-2)
        l.append(d)
        num -= 1
    return f'Сумма {n} элементов геометрической прогресии со знаменателем -1/2 (начиная с 1) равна {sum(l)}'
print(sum_range(100))    
print(timeit.timeit(f'sum_range({100})', setup='from __main__ import sum_range'))

# вместо создания списка, каждый элемент сразу прибавляется к итоговой сумме, сложность снижается, но время почему-то увеличилосьб
def sum_range_new(n):
    num = int(n)
    s=1
    for i in range(1,n):
        s += (-1/2)**i
    return s
print(sum_range_new(100)) 
print(timeit.timeit(f'sum_range_new({100})', setup='from __main__ import sum_range_new'))
