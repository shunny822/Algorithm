import sys
input = sys.stdin.readline

n, m = map(int, input().split())
staff = list(map(int, input().split()))

start = 1
end = max(staff) * m
min_time = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum([mid // staff[i] for i in range(n)])

    if cnt >= m:
        min_time = mid
        end = mid - 1
    else:
        start = mid + 1

print(min_time)
