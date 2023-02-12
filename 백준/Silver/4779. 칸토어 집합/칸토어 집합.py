def cantor(n):
    if not n:
        return '-'
    else:
        c = cantor(n-1)
        can = c + ' '*len(c) + c
        return can

while 1:
    try:
        n = input()
        print(cantor(int(n)))
    except:
        break