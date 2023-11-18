import sys
input = sys.stdin.readline

def dfs(cheese, r, c):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(0, 0)]
    check = [[-1] * c for _ in range(r)]
    check[0][0] = 0
    melting = []

    while stack:
        y, x = stack.pop()
        for dy, dx in delta:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < r and 0 <= nx < c and check[ny][nx] != 0:
                if cheese[ny][nx] == 0:
                    check[ny][nx] = 0
                    stack.append((ny, nx))
                else:
                    if check[ny][nx] > 0:
                        check[ny][nx] += 1
                    else:
                        check[ny][nx] = 1
                    if check[ny][nx] >= 2:
                        melting.append((ny, nx))
                        check[ny][nx] = 0
    return melting

r, c = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(r)]
cnt = 0

while 1:
    melting_cheese = dfs(cheese, r, c)
    if len(melting_cheese) == 0:
        break

    for y, x in melting_cheese:
        cheese[y][x] = 0
    cnt += 1

print(cnt)