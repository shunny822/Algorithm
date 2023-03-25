import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start = 0
end = max(lan)
mid = 1

while 1:
    mid = (end + start) // 2
    if mid == start:
        break

    total = sum([l//mid for l in lan])
    if total >= n:
        start = mid
    else:
        end = mid - 1

if sum([l//end for l in lan]) == n:
    print(end)
else:
    print(mid)