import sys
input = sys.stdin.readline
from collections import deque

front = deque(input().rstrip())
end = deque()

for _ in range(int(input())):
    order = input().rstrip()
    if order == 'L':
        if front:
            end.appendleft(front.pop())
    elif order == 'D':
        if end:
            front.append(end.popleft())
    elif order == 'B':
        if front:
            front.pop()
    else:
        front.append(order[-1])

print(''.join(front+end))