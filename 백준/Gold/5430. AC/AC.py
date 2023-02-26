import sys
intput = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    if n == 0:
        input()
        arr = []
    else:
        a = input().rstrip()
        arr = a[1:len(a)-1].split(',')
    
    is_error = False
    p_list = p.split('R')
    front = 0
    back = 0
    
    for i in range(len(p_list)):
        if i & 1:
            back += len(p_list[i])
        else:
            front += len(p_list[i])

    if front + back > len(arr):
        print('error')
    elif front + back == len(arr):
        print('[]')
    else:
        if len(p_list) % 2 == 0:
            arr = reversed(arr[front:len(arr)-back])
        else:
            arr = arr[front:len(arr)-back]
        print('[', end='')
        print(*arr, sep=',', end=']\n')