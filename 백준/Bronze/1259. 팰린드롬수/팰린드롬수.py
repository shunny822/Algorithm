while 1:
    pal = input()
    if pal == '0':
        break
    if pal[-1] == '0':
        print('no')
    else:
        for i in range(len(pal)//2):
            if pal[i] != pal[-(i+1)]:
                print('no')
                break
        else:
            print('yes')