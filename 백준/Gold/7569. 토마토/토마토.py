import sys
input = sys.stdin.readline
from collections import deque

def bfs(q):
    day = 0

    while q:
        z, y, x, d = q.popleft()
        day = d
        for dz, dy, dx in delta:
            zz = z + dz
            yy = y + dy
            xx = x + dx
            if 0 <= zz < h and 0 <= yy < n and 0 <= xx < m:
                if not check[zz][yy][xx]:
                    check[zz][yy][xx] = True
                    q.append((zz, yy, xx, d+1))
    return day

m, n, h = map(int, input().split())
tomato = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]
check = [list([False] * m for _ in range(n)) for _ in range(h)]
delta = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]
queue = deque([])

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                queue.append((k, i, j, 0))
                check[k][i][j] = True
            elif tomato[k][i][j] == -1:
                check[k][i][j] = True

result = bfs(queue)
if sum([sum([sum(check[k][i]) for i in range(n)]) for k in range(h)]) == h * n * m:
    print(result)
else:
    print(-1)