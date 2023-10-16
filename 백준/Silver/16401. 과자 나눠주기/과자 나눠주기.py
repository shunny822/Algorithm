import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snack = list(map(int, input().split()))
res = 0
s = 1
e = int(1e9)

while s <= e:
    mid = (s+e) // 2
    cnt = 0

    for i in range(n):
        cnt += snack[i] // mid
    
    if cnt >= m:
        res = mid
        s = mid + 1
    else:
        e = mid - 1

print(res)