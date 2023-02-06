import sys

def dfs(x, y):
    stack = [(x, y)]
    check[y][x] = True

    while stack:
        cur_x, cur_y = stack.pop()
        for i in dy:
            for j in dx:
                if 0 <= cur_y+i < h and 0 <= cur_x+j < w:
                    if island[cur_y+i][cur_x+j] == 1 and not check[cur_y+i][cur_x+j]:
                        check[cur_y+i][cur_x+j] = True
                        stack.append((cur_x+j, cur_y+i))


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    island = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    check = [[False]*w for _ in range(h)]
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    cnt = 0

    for y in range(h):
        for x in range(w):
            if island[y][x] and not check[y][x]:
                dfs(x, y)
                cnt += 1
            else:
                continue
    
    print(cnt)