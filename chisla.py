def chisla (a):
    b = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
    if a > 0 and a <= 12:
        return b[a-1]
    else:
        return ' '
while 1:
    print(chisla(int(input())))
