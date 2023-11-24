import sys
input = sys.stdin.readline
from collections import deque

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
cnt = t = 0
bridge = deque([0] * w)

while trucks:
    t += 1
    cnt -= bridge.popleft()

    if cnt + trucks[0] <= l:
        truck = trucks.popleft()
        bridge.append(truck)
        cnt += truck
    else:
        bridge.append(0)

print(t+w)