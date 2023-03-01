import sys
intput = sys.stdin.readline

n = int(input())
l = n // 5
signal = input().rstrip()

x = 0
while x < l:
    if signal[x] == '.':
        x += 1
        continue

    is_one = False
    if x == l - 1:
        for i in range(5):
            if signal[i*l + x] != '#':
                break
        else:
            is_one = True
    else:
        for i in range(5):
            if signal[i*l + x] != '#' or signal[i*l + x+1] != '.':
                break
        else:
            is_one = True
    
    if is_one:
        print(1, end='')
        x += 2
        continue
    
    if x > l - 3:
        break

    if signal[x] == signal[x+1] == signal[x+2] == '#':
        if signal[l+x] == signal[l+x+2] == '#' and signal[l+x+1] == '.':
            if signal[2*l + x+1] == '.':
                print(0, end='')
            elif signal[3*l + x] == '#':
                print(8, end='')
            else:
                print(9, end='')
        elif signal[l+x] == signal[l+x+1] == '.' and signal[l+x+2] == '#':
            if signal[2*l + x] == '.':
                print(7, end='')
            elif signal[3*l + x] == '#':
                print(2, end='')
            else:
                print(3, end='')
        else:
            if signal[3*l + x] == '#':
                print(6, end='')
            else:
                print(5, end='')
    else:
        print(4, end='')
    
    x += 4