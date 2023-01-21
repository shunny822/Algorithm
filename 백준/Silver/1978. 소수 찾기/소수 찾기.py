n = int(input())
nums = list(map(int, input().split()))
if 1 in nums:
    nums.remove(1)
cnt = 0
for i in nums:
    for j in range(2, i//2+1):
        if i % j == 0:
            break
    else:
        cnt += 1
print(cnt)