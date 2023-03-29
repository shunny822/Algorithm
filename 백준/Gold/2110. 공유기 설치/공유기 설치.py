import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start = 1
end = house[-1]
result = 0

while start <= end:
    flag = house[0]
    mid = (start + end) // 2
    cnt = 1

    for i in range(1, n):
        if house[i] - flag >= mid:
            cnt += 1
            flag = house[i]
    
    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)