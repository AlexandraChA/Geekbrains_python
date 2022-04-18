l = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i%j==0:
            l[j-2]+=1
for a in range(len(l)):
    print(f'Количество чисел кратных {a+2} равно {l[a]}')           