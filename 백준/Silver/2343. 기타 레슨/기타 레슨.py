import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lecture = list(map(int, input().split()))
start = max(lecture)
end = sum(lecture)
l = 0

while start <= end:
    mid = (start + end) // 2
    cnt = total = 0

    for i in range(n):
        if total + lecture[i] > mid:
            cnt += 1
            total = lecture[i]
        else:
            total += lecture[i]
    
    if cnt + 1 <= m:
        l = mid
        end = mid - 1
    else:
        start = mid + 1

print(l)