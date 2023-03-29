import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]
start = 1
end = max(time) * m // n + 1
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum([mid // time[i] for i in range(n)])
    if cnt >= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)