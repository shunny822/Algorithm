nums = [int(input()) for _ in range(10)]
print(sum(nums)//10)

n_dict = {}
for i in range(10):
    if nums[i] in n_dict:
        n_dict[nums[i]] += 1
    else:
        n_dict[nums[i]] = 1

freq = sorted(n_dict.items(), key=lambda x: x[1], reverse=True)
print(freq[0][0])