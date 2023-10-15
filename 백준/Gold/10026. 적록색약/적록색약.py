import sys
input = sys.stdin.readline

def dfs(i, j, target):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(i, j)]

    while stack:
        y, x = stack.pop()
        for dy, dx in delta:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n and not check[ny][nx] and matrix[ny][nx] in target:
                check[ny][nx] = True
                stack.append((ny, nx))

n = int(input())
matrix = [input().strip() for _ in range(n)]
normal = 0
sick = 0

check = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not check[i][j]:
            check[i][j] = True
            dfs(i, j, {matrix[i][j]})
            normal += 1

check = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not check[i][j]:
            check[i][j] = True
            if matrix[i][j] == 'B':
                dfs(i, j, {'B'})
            else:
                dfs(i, j, {'R', 'G'})
            sick += 1

print(normal, sick)