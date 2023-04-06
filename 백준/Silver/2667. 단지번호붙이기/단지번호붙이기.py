import sys
input = sys.stdin.readline

def dfs(y, x, cnt):
    check[y][x] = True
    cnt += 1
    for dy, dx in delta:
        ny = y + dy
        nx = x + dx
        if ny >= 0 and ny < n and nx >= 0 and nx < n:
            if village[ny][nx] == '1' and not check[ny][nx]:
                cnt = dfs(ny, nx, cnt)
    return cnt

n = int(input())
village = [input().rstrip() for _ in range(n)]
check = [[False] * n for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
total = []

for i in range(n):
    for j in range(n):
        if village[i][j] == '1' and not check[i][j]:
            total.append(dfs(i, j, 0))

print(len(total))
print(*sorted(total), sep='\n')