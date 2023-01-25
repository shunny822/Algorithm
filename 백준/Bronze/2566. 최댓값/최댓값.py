import sys

nums = []
biggest_n = 0
n_index = 0
for i in range(9):
    nums.append(list(map(int, sys.stdin.readline().split())))
    big_n = max(nums[i])
    if big_n > biggest_n:
        biggest_n = big_n
        n_index = i

print(biggest_n)
print(n_index+1, nums[n_index].index(biggest_n)+1)