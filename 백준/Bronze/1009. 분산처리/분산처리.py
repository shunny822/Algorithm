import sys
intput = sys.stdin.readline

l = [(1, [0]), (1, [1]), (4, [6, 2, 4, 8]), (4, [1, 3, 9, 7]), (2, [6, 4]), (1, [5]),
    (1, [6]), (4, [1, 7, 9, 3]), (4, [6, 8, 4, 2]), (2, [1, 9])]
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    else:
        b %= l[a][0]
        print(l[a][1][b])