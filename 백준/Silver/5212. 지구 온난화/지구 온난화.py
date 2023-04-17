import sys
input = sys.stdin.readline

def delta_explore(y, x):
    cnt = 0
    for dy, dx in delta:
        ny = y + dy
        nx = x + dx
        if ny >= 0 and ny < r and nx >= 0 and nx < c:
            if island[ny][nx] == 'X':
                cnt += 1
    return cnt

r, c = map(int, input().split())
island = [input().rstrip() for _ in range(r)]
check = [[False] * c for _ in range(r)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(r):
    for j in range(c):
        if island[i][j] == 'X' and delta_explore(i, j) >= 2:
            check[i][j] = True

min_y = max_y = min_x = max_x = 0
for i in range(r):
    min_y = i
    if sum(check[i]) > 0:
        break
for i in reversed(range(r)):
    max_y = i
    if sum(check[i]) > 0:
        break
for j in range(c):
    min_x = j
    cnt = 0
    for i in range(r):
        cnt += check[i][j]
    if cnt > 0:
        break
for j in reversed(range(c)):
    max_x = j
    cnt = 0
    for i in range(r):
        cnt += check[i][j]
    if cnt > 0:
        break

for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        if check[y][x]:
            print('X', end='')
        else:
            print('.', end='')
    print()