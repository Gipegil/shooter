a = int(input())
b = 0
c = 0
while a == 0:
    a = int(input('Ошибка'))
while a != 0:
    c += 1
    b += a
    a = int(input())
print(str(b/c))


a = input()
b = 0
for i in range(len(a)):
    b += int(a[i])
print(b)
