n = int(input())
while 1:
    nums = set(str(n))
    if len(nums) == 2:
        if '4' in nums and '7' in nums:
            break
        else:
            n -=1
    elif len(nums) == 1:
        if '4' in nums or '7' in nums:
            break
        else:
            n -=1
    else:
        n -= 1

print(n)