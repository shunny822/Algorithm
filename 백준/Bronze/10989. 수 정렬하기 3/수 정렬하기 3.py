import sys
input = sys.stdin.readline

n = int(input())
nums = {}
for _ in range(n):
    x = int(input())
    nums[x] = nums.get(x, 0) + 1

for num in sorted(nums.keys()):
    for _ in range(nums[num]):
        print(num)