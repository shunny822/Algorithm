a, b = map(int, input().split())

if abs(a - b) == 1:
    if a > b:
        print('A')
    else:
        print('B')
else :
    if a == 1:
        print('A')
    else:
        print('B')