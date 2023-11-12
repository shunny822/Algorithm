import sys
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def spread(matrix, r, c):
    new_matrix = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            space = matrix[y][x]
            if space > 0:
                dust = space // 5
                for dy, dx in delta:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < r and 0 <= nx < c and matrix[ny][nx] != -1:
                        new_matrix[ny][nx] += dust
                        space -= dust
                new_matrix[y][x] += space
    return new_matrix

def clean_room(cleaner, matrix, r, c):
    up_y, up_x = cleaner[0]
    down_y, down_x = cleaner[1]
    # ↓ ↑
    for i in range(up_y-1, 0, -1):
        matrix[i][0] = matrix[i-1][0]
        matrix[i-1][0] = 0
    for i in range(down_y+1, r-1):
        matrix[i][0] = matrix[i+1][0]
        matrix[i+1][0] = 0
    # ←
    matrix[0].pop(up_x)
    matrix[0].append(0)
    matrix[r-1].pop(down_x)
    matrix[r-1].append(0)
    # ↑ ↓
    for i in range(0, up_y):
        matrix[i][c-1] = matrix[i+1][c-1]
        matrix[i+1][c-1] = 0
    for i in range(r-1, down_y, -1):
        matrix[i][c-1] = matrix[i-1][c-1]
        matrix[i-1][c-1] = 0
    # →
    matrix[up_y].pop()
    matrix[up_y].insert(up_x+1, 0)
    matrix[down_y].pop()
    matrix[down_y].insert(down_x+1, 0)

    return matrix

r, c, t = map(int, input().split())
room = []
cleaner = []
for i in range(r):
    line = list(map(int, input().split()))
    for j, l in enumerate(line):
        if l == -1:
            cleaner.append((i, j))
    room.append(line)

for _ in range(t):
    room = spread(room, r, c)
    for y, x in cleaner:
        room[y][x] = -1
    room = clean_room(cleaner, room, r, c)

print(sum([sum(l) for l in room])+2)