a = 0
b = float(input("Объем бутылки(0-стоп)"))
while b != 0:
    if b <= 1:
        a += 0.10
    else:
        a += 0.25
    b = float(input("Объем бутылки"))
print('$'+str(a))
