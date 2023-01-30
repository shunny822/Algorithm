import sys

dots = []
for _ in range(4):
    dots.append(list(map(int, sys.stdin.readline().split())))

n = m = 0
for i in range(4):
    if dots[i][2] > n:
        n = dots[i][2]
    if dots[i][3] > m:
        m = dots[i][3]

width = [[0]*n for _ in range(m)]
for i in range(4):
    for y in range(dots[i][1],dots[i][3]):
        for x in range(dots[i][0], dots[i][2]):
            width[y][x] = 1

total = 0
for line in width:
    total += sum(line)
print(total)