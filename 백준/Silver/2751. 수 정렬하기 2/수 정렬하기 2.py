import sys

n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]
print(*sorted(nums), sep='\n')