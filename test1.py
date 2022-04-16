a = input("Имя")
c = input("Результат")
b = dict()
while a != '0':
    b[a] = c
    a = input('Имя')
    if a == '0':
        break
    c = input('Результат')
print(b)
