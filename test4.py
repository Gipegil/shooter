def pasport (a):
    if a >= 14:
        return 1

if pasport(int(input())):
    print('Паспорт есть')
else:
    print("Паспорта нет")


def dostavka(a):
    b = 0
    if a >= 1:
        b += 10.95
    b += (a-1)*2.95
    return b
print('$'+str(dostavka(int(input()))))
