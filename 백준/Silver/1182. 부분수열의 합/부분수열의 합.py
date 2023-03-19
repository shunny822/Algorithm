import itertools
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    for nums in itertools.combinations(numbers, i):
        if sum(nums) == s:
            cnt += 1
print(cnt)