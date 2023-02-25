n, k = map(int, input().split())
nums = [0 for _ in range(n+1)]
cnt = 0

for i in range(2, n+1):
    if nums[i] == 1:
        continue
    if cnt == k:
        break

    for j in range(i, n+1, i):
        if nums[j] == 0:
            nums[j] = 1
            cnt += 1
        if cnt == k:
            print(j)
            break