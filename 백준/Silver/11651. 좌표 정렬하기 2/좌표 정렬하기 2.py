import sys

n = int(input())
nums = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
nums.sort(key=lambda x:(x[1], x[0]))
for num in nums:
    print(*num)