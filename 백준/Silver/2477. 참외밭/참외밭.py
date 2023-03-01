import sys
intput = sys.stdin.readline
from collections import deque

n = int(input())
farm = deque()
h = 0
w = 0
for _ in range(6):
    a, b = map(int, input().split())
    farm.append((a, b))
    if a <= 2 and b > w:
        w = b
    elif a > 2 and b > h:
        h = b

for i in range(6):
    if (farm[i-1][1] == h and farm[i][1] == w) or (farm[i-1][1] == w and farm[i][1] == h):
        if i < 2:
            while i > -1:
                farm.append(farm.popleft())
                i -= 1
        else:
            while i < 5:
                farm.appendleft(farm.pop())
                i += 1
        break

print(n * (h * w - (farm[1][1] * farm[2][1])))