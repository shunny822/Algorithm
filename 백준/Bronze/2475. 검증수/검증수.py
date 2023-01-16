nums = list(map(int, input().split()))
total = 0
for n in nums:
    total += n**2
print(total%10)