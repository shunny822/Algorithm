import sys
from collections import deque

def jump(b, a):
    q = deque([(b, a)])

    while q:
        y, x = q.popleft()

        # 목적지 도착
        if matrix[y][x] == -1:
            return print('HaruHaru')
        # 0이면 무시
        elif matrix[y][x] == 0:
            continue
        else:
            v = matrix[y][x]
            matrix[y][x] = 0   # 방문처리

            # 인덱스 범위 내일 경우 덱에 추가
            if 0 <= y+v < n:
                q.append((y+v, x))
            if 0 <= x+v < n:
                q.append((y, x+v))
    else:
        return print('Hing')

n = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
jump(0, 0)