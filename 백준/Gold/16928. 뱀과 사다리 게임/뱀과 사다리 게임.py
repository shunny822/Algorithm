import sys
input = sys.stdin.readline
from collections import deque

def find_turn(up: dict, down: dict):
    check = [False] * 101
    check[1] = True
    q = deque([(1, 0)])

    while q:
        location, turn = q.popleft()
        
        for i in range(1, 7):
            temp = location + i

            if temp >= 100:
                return print(turn + 1)
            
            if check[temp]:
                continue

            if temp in up:
                temp = up[temp]
            elif temp in down:
                temp = down[temp]
            
            check[temp] = True
            q.append((temp, turn+1))


n, m = map(int, input().split())
ladder = {}
snake = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

find_turn(ladder, snake)