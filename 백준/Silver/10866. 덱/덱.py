import sys
from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    order = sys.stdin.readline().rstrip()
    if 'push_front' in order:
        order, n = order.split()
        d.appendleft(n)
    elif 'push_back' in order:
        order, n = order.split()
        d.append(n)
    elif order == 'pop_front':
        print(d.popleft() if d else -1)
    elif order == 'pop_back':
        print(d.pop() if d else -1)
    elif order == 'size':
        print(len(d))
    elif order == 'empty':
        print(0 if d else 1)
    elif order == 'front':
        print(d[0] if d else -1)
    elif order == 'back':
        print(d[-1] if d else -1)