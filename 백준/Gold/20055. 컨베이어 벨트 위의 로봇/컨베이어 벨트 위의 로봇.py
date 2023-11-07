import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
l = list(map(int, input().split()))
upper_belt = deque(l[:n])
robot = deque([False] * n)
lower_belt = deque(l[n:][::-1])

turn = 0
zero = 0
while zero < k:
    turn += 1
    lower_belt.append(upper_belt.pop())
    upper_belt.appendleft(lower_belt.popleft())
    robot.pop()
    robot.appendleft(False)
    robot[-1] = False

    for i in range(n-1, 0, -1):
        if robot[i-1] and upper_belt[i] > 0 and not robot[i]:
            robot[i-1] = False
            upper_belt[i] -= 1
            robot[i] = True
            if upper_belt[i] == 0:
                zero += 1
    robot[n-1] = False

    if upper_belt[0] > 0:
        upper_belt[0] -= 1
        robot[0] = True
        if upper_belt[0] == 0:
            zero += 1
    
print(turn)