import sys
input = sys.stdin.readline

def change_office(y, x, dy, dx, office):
    changes = []

    while 0 <= y < n and 0 <= x < m:
        if office[y][x] == 0:
            changes.append((y, x))
            office[y][x] = '#'
        elif office[y][x] == 6:
            break
        y += dy
        x += dx

    return changes


def revert_office(changes, office):
    for y, x in changes:
        office[y][x] = 0


def observation(cctv, turn, office, res):
    if turn == len(cctv):
        res.append(sum([line.count(0) for line in office]))
        return
    
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    y, x = cctv[turn]
    
    if office[y][x] == 1:
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            changes = change_office(ny, nx, dy, dx, office)
            observation(cctv, turn+1, office, res)
            revert_office(changes, office)
    elif office[y][x] == 2:
        for i in range(2):
            changes = []
            dy, dx = delta[i]
            change = change_office(y+dy, x+dx, dy, dx, office)
            changes += change
            dy, dx = delta[i+2]
            change = change_office(y+dy, x+dx, dy, dx, office)
            changes += change
            observation(cctv, turn+1, office, res)
            revert_office(changes, office)
    elif office[y][x] == 3:
        for i in range(4):
            changes = []
            for j in range(2):
                dy, dx = delta[(i+j)%4]
                change = change_office(y+dy, x+dx, dy, dx, office)
                changes += change
            observation(cctv, turn+1, office, res)
            revert_office(changes, office)
    elif office[y][x] == 4:
        for i in range(4):
            changes = []
            for j in range(3):
                dy, dx = delta[(i+j)%4]
                change = change_office(y+dy, x+dx, dy, dx, office)
                changes += change
            observation(cctv, turn+1, office, res)
            revert_office(changes, office)
    elif office[y][x] == 5:
        changes = []
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            change = change_office(ny, nx, dy, dx, office)
            changes += change
        observation(cctv, turn+1, office, res)
        revert_office(changes, office)


n, m = map(int, input().split())

office = []
cctv = []
res = []

for i in range(n):
    line = list(map(int, input().split()))
    office.append(line)

    for j in range(m):
        if line[j] not in {0, 6}:
            cctv.append((i, j))

observation(cctv, 0, office, res)
print(min(res))