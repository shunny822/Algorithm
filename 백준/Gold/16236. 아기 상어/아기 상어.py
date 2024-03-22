import sys
input = sys.stdin.readline
from collections import deque

def bfs(space, n, i, j, shark):
    delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    check = [[False] * n for _ in range(n)]
    q = deque([(i, j, 0)])
    check[i][j] = True
    eat = []

    while q:
        y, x, turn = q.popleft()

        for dy, dx in delta:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < n and not check[ny][nx] and space[ny][nx] <= shark:
                q.append((ny, nx, turn+1))
                check[ny][nx] = True

                if 0 < space[ny][nx] < shark:
                    eat.append((turn+1, ny, nx))

    if eat:
        eat.sort()
        turn, y, x = eat[0]
        space[i][j] = 0
        space[y][x] = 9
        return y, x, turn
    else:
        return i, j, 0


def solve():
    n = int(input())
    space = []
    s_y = s_x = 0

    for i in range(n):
        row = list(map(int, input().split()))
        space.append(row)

        for j in range(n):
            if row[j] == 9:
                s_y, s_x = i, j

    sec = 0
    shark = 2
    fish_cnt = 0

    while 1:
        s_y, s_x, res = bfs(space, n, s_y, s_x, shark)

        if res > 0:
            sec += res
            fish_cnt += 1

            if fish_cnt == shark:
                shark += 1
                fish_cnt = 0
        else:
            break

    print(sec)


solve()