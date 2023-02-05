import sys
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    order = sys.stdin.readline().rstrip()
    if 'push' in order:
        order, x = order.split()
        q.append(x)
    elif order == 'pop':
        print(q.popleft() if q else -1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        print(0 if q else 1)
    elif order == 'front':
        print(q[0] if q else -1)
    elif order == 'back':
        print(q[-1] if q else -1)