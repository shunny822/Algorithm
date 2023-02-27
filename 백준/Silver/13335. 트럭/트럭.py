import sys
from collections import deque
intput = sys.stdin.readline

n, length, wt = map(int, input().split())
truck = deque(map(int, input().split()))
done = deque()
on_bridge = 0
cnt = 0

while truck:
    if len(done) < length - 1:
        if on_bridge + truck[0] <= wt:
            x = truck.popleft()
            done.append(x)
            on_bridge += x
        else:
            done.append(0)
    else:
        if on_bridge + truck[0] <= wt:
            x = truck.popleft()
            done.append(x)
            on_bridge = on_bridge + x - done.popleft()
        else:
            done.append(0)
            on_bridge -= done.popleft()
    cnt += 1

print(cnt + length)