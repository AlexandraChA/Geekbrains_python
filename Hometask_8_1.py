import hashlib
substrings = []
string = input('Введите строку из маленьких латинских букв: ')
for i in range(len(string)):
    for j in range(len(string), i, -1):
        substrings.append(string[i:j])
    substrings = list(set(substrings)) 
for i in substrings:
    i = hashlib.md5((i).encode('utf-8')).hexdigest() 
print(f'Количество подстрок в строке {string} равно {len(substrings)}')