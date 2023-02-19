import sys
input = sys.stdin.readline
from collections import deque

def bfs(y, x):
    q = deque([(y, x)])
    check[y][x] = True

    while q:
        y, x = q.popleft()
        if y == n-1 and x == m-1:
            break
        for dy, dx in delta:
            if 0 <= y+dy < n and 0 <= x+dx < m:
                if maze[y+dy][x+dx] and not check[y+dy][x+dx]:
                    maze[y+dy][x+dx] = maze[y][x] + 1
                    check[y+dy][x+dx] = True
                    q.append((y+dy, x+dx))
    return

n, m = map(int, input().split())
maze = [[int(i) for i in list(input().rstrip())] for _ in range(n)]
check = [[False] * m for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bfs(0, 0)
print(maze[n-1][m-1])