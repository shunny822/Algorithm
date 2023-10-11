import sys
from itertools import combinations as cb
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

blank = []
virus = deque()
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            blank.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

res = 0
for walls in cb(blank, 3):
    test_lab = copy.deepcopy(lab)
    q = copy.copy(virus)
    for y, x in walls:
        test_lab[y][x] = 1

    delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    while q:
        y, x = q.popleft()
        for dy, dx in delta:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < n and 0 <= nx < m and test_lab[ny][nx] == 0:
                test_lab[ny][nx] = 2
                q.append((ny, nx))
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if test_lab[i][j] == 0:
                cnt += 1

    res = max(cnt, res)
            
print(res)