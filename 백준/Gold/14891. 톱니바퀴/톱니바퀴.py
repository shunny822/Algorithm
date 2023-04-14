import sys
input = sys.stdin.readline
from collections import deque

wheel = [0]
for _ in range(4):
    wheel.append(deque(input().rstrip()))

k = int(input())
for _ in range(k):
    dir = [0] * 5
    n, d = map(int, input().split())
    dir[n] = d

    index = n - 1
    flag = wheel[n][6]
    while index > 0:
        if wheel[index][2] != flag:
            if dir[index+1] == 1:
                dir[index] = -1
            elif dir[index+1] == -1:
                dir[index] = 1
        flag = wheel[index][6]
        index -= 1

    index = n + 1
    flag = wheel[n][2]
    while index < 5:
        if wheel[index][6] != flag:
            if dir[index-1] == 1:
                dir[index] = -1
            elif dir[index-1] == -1:
                dir[index] = 1
        flag = wheel[index][2]
        index += 1

    for i in range(1, 5):
        wheel[i].rotate(dir[i])

ans = 0
for i in range(1, 5):
    if wheel[i][0] == '1':
        ans += 2 ** (i-1)
print(ans)