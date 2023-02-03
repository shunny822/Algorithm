import sys
from collections import deque

n, m = map(int, input().split())
que = deque(range(1, n+1))
pick = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in pick:
    if que.index(i) < n/2:
        while que[0] != i:
            que.append(que.popleft())
            cnt += 1
    else:
        while que[0] != i:
            que.appendleft(que.pop())
            cnt += 1
    que.popleft()
    n -= 1

print(cnt)