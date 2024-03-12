import sys
input = sys.stdin.readline

def melt():
    melting_ice = []

    for y in range(n):
        for x in range(m):
            if ice[y][x] == 0:
                for dy, dx in delta:
                    ny, nx = y + dy, x + dx

                    if 0 <= ny < n and 0 <= nx < m and ice[ny][nx] > 0:
                        melting_ice.append((ny, nx))
    
    for y, x in melting_ice:
        if ice[y][x] > 0:
            ice[y][x] -= 1


def check_piece(i, j, check):
    check[i][j] = True
    stack = [(i, j)]

    while stack:
        y, x = stack.pop()

        for dy, dx in delta:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m and ice[ny][nx] > 0 and not check[ny][nx]:
                check[ny][nx] = True
                stack.append((ny, nx))
                


n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
year = 0

while 1:
    melt()
    year += 1

    c = [[False] * m for _ in range(n)]
    piece = 0

    for y in range(n):
        for x in range(m):
            if ice[y][x] > 0 and not c[y][x]:
                check_piece(y, x, c)
                piece += 1
    
    if piece >= 2:
        print(year)
        break
    elif piece == 0:
        print(0)
        break