import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

nums = {}
for i in range(-k, 0):
    nums[sushi[i]] = nums.get(sushi[i], 0) + 1

ans = len(nums) if c in nums else len(nums) + 1

for j in range(n):
    if nums[sushi[j-k]] == 1:
        nums.pop(sushi[j-k])
    else:
        nums[sushi[j-k]] -= 1

    nums[sushi[j]] = nums.get(sushi[j], 0) + 1
    ans = max(ans, len(nums)) if c in nums else max(ans, len(nums) + 1)

print(ans)