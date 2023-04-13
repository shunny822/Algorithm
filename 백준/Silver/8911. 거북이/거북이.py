import sys
input = sys.stdin.readline

t = int(input())
way = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(t):
    d = 0
    min_y = max_y = min_x = max_x = 0
    y = x = 0
    order = input().rstrip()
    for o in order:
        if o == 'F':
            dy, dx = way[d]
            y += dy
            x += dx
        elif o == 'B':
            dy, dx = way[d]
            y -= dy
            x -= dx
        elif o == 'L':
            d = (d + 3) % 4
        else:
            d = (d + 5) % 4
        
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        max_x = max(max_x, x)
    print((max_y - min_y) * (max_x - min_x))