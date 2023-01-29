import sys
from collections import deque

n = int(input())
nums = deque()
for _ in range(n):
    order = sys.stdin.readline().rstrip()
    if 'push' in order:
        order, x = order.split()
        nums.append(int(x))
    elif order == 'pop':
        print(nums.popleft() if nums else -1)
    elif order == 'size':
        print(len(nums))
    elif order == 'empty':
        print(0 if nums else 1)
    elif order == 'front':
        print(nums[0] if nums else -1)
    elif order == 'back':
        print(nums[-1] if nums else -1)