import sys
input = sys.stdin.readline

n, h = map(int, input().split())
down = [0] * (h+1)
up = [0] * (h+1)

for i in range(n):
    height = int(input())
    if i % 2 == 0:
        down[height] += 1
    else:
        up[height] += 1

for i in range(h-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

min_count = n
same_height = 0

for i in range(1, h+1):
    if (min_count > down[i] + up[h - i + 1]):
        min_count = down[i] + up[h - i + 1]
        same_height = 1
    elif (min_count == down[i] + up[h - i + 1]):
        same_height += 1

print(min_count, same_height)