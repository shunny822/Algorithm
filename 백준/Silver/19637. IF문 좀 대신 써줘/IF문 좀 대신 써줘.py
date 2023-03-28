import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tier = {}
for _ in range(n):
    name, score = input().split()
    if int(score) not in tier:
        tier[int(score)] = name

level = sorted(tier.keys())
power = [int(input()) for _ in range(m)]

for p in power:
    start = 0
    end = len(level) - 1
    my_level = 0

    while start <= end:
        mid = (start + end) // 2

        if level[mid] >= p:
            my_level = level[mid]
            end = mid -1
        else:
            start = mid + 1
        
    print(tier[my_level])