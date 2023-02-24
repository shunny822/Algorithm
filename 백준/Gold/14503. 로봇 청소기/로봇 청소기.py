import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0

while 1:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    is_be = False
    for dy, dx in delta:
        ny = r + dy
        nx = c + dx
        if 0 <= ny < n and 0 <= nx < m:
            if room[ny][nx] == 0:
                is_be = True

    if is_be:
        for i in range(1, 5):
            dy, dx = delta[(d+4-i)%4]
            if room[r+dy][c+dx] == 0:
                r = r + dy
                c = c + dx
                d = d + 4 - i
                break
    else:
        dy, dx = delta[(d+2)%4]
        if room[r+dy][c+dx] != 1:
            r = r + dy
            c = c + dx
        else:
            break

print(cnt)