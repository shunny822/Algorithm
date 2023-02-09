import sys

n = int(input())
nums = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
nums.sort()
for t in nums:
    print(*t)