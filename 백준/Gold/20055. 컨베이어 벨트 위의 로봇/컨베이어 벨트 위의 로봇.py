import sys
input = sys.stdin.readline
from collections import deque

n, k= map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([False] * 2 * n)
cnt = turn = 0

while cnt < k:
    turn += 1
    belt.appendleft(belt.pop())
    robots.appendleft(robots.pop())
    robots[n-1] = False

    for i in reversed(range(n-1)):
        if robots[i] and not robots[i+1] and belt[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            belt[i+1] -= 1
            if belt[i+1] == 0:
                cnt += 1
    
    robots[n-1] = False

    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1

print(turn)