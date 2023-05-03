import sys
input = sys.stdin.readline

delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), ]
n, m = map(int, input().split())

basket = [list(map(int, input().split())) for _  in range(n)]
cloud = [[False] * n for _ in range(n)]

for i in range(n-2, n):
    for j in range(2):
        cloud[i][j] = True

for _ in range(m):
    d, s = map(int, input().split())
    d -= 1
    dy, dx = delta[d]
    temp = []
    for y in range(n):
        for x in range(n):
            if cloud[y][x] == True:
                cloud[y][x] = False
                ny = (n + y + dy*s) % n
                nx = (n + x + dx*s) % n
                temp.append((ny, nx))
    
    for y, x in temp:
        cloud[y][x] = True
        basket[y][x] += 1

    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                cnt = 0
                for di, dj in delta[1::2]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < n and basket[ni][nj] != 0:
                        cnt += 1
                basket[i][j] += cnt

    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                cloud[i][j] = False
            elif basket[i][j] >= 2:
                basket[i][j] -= 2
                cloud[i][j] = True
    
print(sum([sum(line) for line in basket]))