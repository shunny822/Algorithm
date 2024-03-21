import sys
input = sys.stdin.readline
from collections import deque

def crush(field, check, i, j, is_crushed):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    temp = [(i, j)]
    q = deque([(i, j)])
    check[i][j] = True

    while q:
        y, x = q.popleft()
        
        for dy, dx in delta:
            ny, nx = y + dy, x + dx

            if 0 <= ny < 12 and 0 <= nx < 6 and field[ny][nx] == field[i][j] and not check[ny][nx]:
                temp.append((ny, nx))
                check[ny][nx] = True
                q.append((ny, nx))
    
    if len(temp) >= 4:
        is_crushed = True

        for y, x in temp:
            field[y][x] = '.'
    
    return is_crushed


def explore(field, is_crushed):
    check = [[False] * 6 for _ in range(12)]
    
    for y in range(12):
        for x in range(6):
            if field[y][x] != '.' and not check[y][x]:
                is_crushed = crush(field, check, y, x, is_crushed)

    return is_crushed


def down(field):
    for x in range(6):
        remain = [field[y][x] for y in reversed(range(12)) if field[y][x] != '.']
        l = len(remain)

        for y in range(l):
            field[11-y][x] = remain[y]
        
        for y in range(12 - l):
            field[y][x] = '.'


def solve():
    field = [list(input().rstrip()) for _ in range(12)]
    turn = 0

    while 1:
        is_crushed = explore(field, False)

        if is_crushed:
            turn += 1
        else:
            break

        down(field)

    print(turn)


solve()