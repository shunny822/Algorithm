n, k = map(int, input().split())
start = 0
end = n//2 + 1
while start <= end:
    mid = (start + end) // 2
    paper = (mid + 1) * (n - mid + 1)
    if paper == k:
        print('YES')
        break
    elif paper < k:
        start = mid + 1
    else:
        end = mid - 1
else:
    print('NO')