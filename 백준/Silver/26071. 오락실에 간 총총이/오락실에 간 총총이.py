import sys
input = sys.stdin.readline

n = int(input())
gom_x = set()
gom_y = set()

for i in range(n):
    line = input().rstrip()
    for j in range(n):
        if line[j] == 'G':
            gom_x.add(j)
            gom_y.add(i)

if len(gom_x) == len(gom_y) == 1:
    print(0)
else:
    list_x = list(gom_x)
    list_x.sort()
    list_y = list(gom_y)
    list_y.sort()

    if len(gom_x) == 1:
        print(min(n-1-list_y[0], list_y[-1]))
    elif len(gom_y) == 1:
        print(min(n-1-list_x[0], list_x[-1]))
    else:
        print(min(n-1-list_y[0], list_y[-1]) + min(n-1-list_x[0], list_x[-1]))