def chisla (a):
    b = ['one','two','three','four','five','six','seven','eight','nine']
    c = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    t = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    f = ''
    if a < 0 or a > 999:
        return 0
    s = len(str(a))
    r = str(a)
    if s == 3:
        f += b[int(r[0])-1] +' '
        f += 'hundred '
        f += c[int(r[1])-2] +' '
        f += b[int(r[2])-1] +' '
    if s == 2:
        if a == 10:
            f = 'ten'
        elif a > 10 and a < 20:
            f = t[int(r[1])-1]
        else:
            f += c[int(r[0])-2] +' '
            f += b[int(r[1])-1] +' '
    if s == 1:
        f += b[int(r[0])-1] +' '
    return f
    
while 1:
    try:
        print(chisla(int(input())))
    except:
        print(':(')
