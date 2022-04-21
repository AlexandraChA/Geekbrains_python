import timeit
# алгоритм нахождения i-ого простого числа без использования "решета Эратосфена"
# квадратичная сложность, так как вложенные циклы
def prime_num(i):
    l=[]
    for x in range(2, i+1):
        flag=True
        for j in range(2,x):
            if i%j==0:
                flag = False
                break
        if flag == True:
            l.append(x) 
    return l[-1]                
print(timeit.timeit(f'prime_num({500})', setup ='from __main__ import prime_num'))

# тот же алгоритм, но с использованием решета Эратосфена
# вложенные циклы остались, однако прохождение идет по уже существующему массиву, что упрощает задачу
def prime_num_eratosfen(i):
    l=[x for x in range(2, i+1)]
    for num in l:
        for j in range(2*num, len(l), num):
            l.remove(j)
    return l[-1]             
print(timeit.timeit(f'prime_num_eratosfen({500})', setup ='from __main__ import prime_num_eratosfen'))