import sys
input = sys.stdin.readline

def dfs(y, x):
    stack = [(y, x)]
    check[y][x] = True
    index = [(y, x)]
    total = country[y][x]
    
    while stack:
        y, x = stack.pop()
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n and not check[ny][nx] and l <= abs(country[y][x] - country[ny][nx]) <= r:
                check[ny][nx] = True
                stack.append((ny, nx))
                index.append((ny, nx))
                total += country[ny][nx]

    res = total // len(index)
    for yi, xi in index:
        country[yi][xi] = res
    return

n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0

while 1:
    check = [[False] * n for _ in range(n)]
    is_changed = False

    for i in range(n):
        for j in range(n):
            if check[i][j]:
                is_changed = True
            else:
                dfs(i, j)
    if is_changed:
        cnt += 1
    else:
        break
print(cnt)