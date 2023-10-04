import sys
input = sys.stdin.readline

def dfs(arr, a, b):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = [(a, b)]
    arr[a][b] = 1
    volume = 1

    while stack:
        y, x = stack.pop()
        
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < m and 0 <= nx < n and arr[ny][nx] == 0:
                arr[ny][nx] = 1
                stack.append((ny, nx))
                volume += 1

    return (arr, volume)

m, n, k = map(int, input().split())
matrix = [[0] * n for _ in range(m)]

for i in range(k):
    xs, ys, xe, ye = map(int, input().split())
    for y in range(ys, ye):
        for x in range(xs, xe):
            matrix[y][x] = 1

cnt = 0
v_arr = []

for y in range(m):
    for x in range(n):
        if matrix[y][x] == 0:
            cnt += 1
            matrix, v = dfs(matrix, y, x)
            v_arr.append(v)

print(cnt)
v_arr.sort()
print(*v_arr)