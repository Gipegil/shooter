if int(input()) % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
        
a = ['a','e','i','o','u']
b = input()
if b != 'y':
    if b not in a:
        print('Согл.')
    else:
        print('Глас.')
else:
    print('Глас. и Согл.')
