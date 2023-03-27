import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())
box = [int(input()) for _ in range(m)]
start = 1
end = max(box)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum([math.ceil((b) / mid) for b in box])

    if cnt <= n:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)