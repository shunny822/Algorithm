import sys
input = sys.stdin.readline
from collections import deque

def jump(b, a):
    q = deque([(b, a)])

    while q:
        y, x = q.popleft()
        v = matrix[y][x]
        if not v:
            return print('Hing')

        if y+v == x == n-1:
            return print('HaruHaru')
        elif 0 <= y+v < n:
            q.append((y+v, x))
        if y == x+v == n-1:
            return print('HaruHaru')
        elif 0 <= x+v < n:
            q.append((y, x+v))
    else:
        return print('Hing')

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
jump(0, 0)