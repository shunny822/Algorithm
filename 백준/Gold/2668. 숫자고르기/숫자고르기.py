import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
pair_nums = [0] * (n+1)
n_cnt = {}
for i in range(n):
    a = int(input())
    pair_nums[i+1] = a
    n_cnt[a] = n_cnt.get(a, 0) + 1

second_line = n_cnt.keys()
for i in range(1, n+1):
    if i not in second_line:
        n_cnt[pair_nums[i]] -= 1

to_delete = deque()
for key in second_line:
    if n_cnt[key] <= 0:
        to_delete.append(key)

while to_delete:
    x = to_delete.popleft()
    if x in n_cnt:
        n_cnt.pop(x)
        pair = pair_nums[x]
        if pair in n_cnt:
            n_cnt[pair] -= 1
            if n_cnt[pair] <= 0:
                to_delete.append(pair)

print(len(n_cnt))
for k in sorted(n_cnt.keys()):
    print(k)