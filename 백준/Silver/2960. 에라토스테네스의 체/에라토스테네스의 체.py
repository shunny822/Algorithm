n, k = map(int, input().split())
nums = [i for i in range(2, n+1)]
cnt = 0

while cnt < k:
    x = nums[0]
    for i in range(len(nums)):
        if i >= len(nums):
            break
        
        if nums[i] % x == 0:
            cnt += 1
            if cnt == k:
                print(nums.pop(i))
                break
            else:
                nums.pop(i)