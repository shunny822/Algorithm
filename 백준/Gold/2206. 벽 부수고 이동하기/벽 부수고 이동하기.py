import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
matrix = [input().rstrip() for _ in range(n)]
check = [[[0] * 2 for _ in range(m)] for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

check[0][0][0] = 1
queue = deque([(0, 0, 0)])
ans = -1

while queue:
    y, x, wall = queue.popleft()

    if y == n-1 and x == m-1:
        ans = check[y][x][wall]
        break

    for dy, dx in delta:
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < m and not check[ny][nx][wall]:
            if matrix[ny][nx] == '1' and wall == 0:
                queue.append((ny, nx, 1))
                check[ny][nx][1] = check[y][x][0] + 1
            elif matrix[ny][nx] == '0':
                queue.append((ny, nx, wall))
                check[ny][nx][wall] = check[y][x][wall] + 1

print(ans)