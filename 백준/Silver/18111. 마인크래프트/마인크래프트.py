import sys
intput = sys.stdin.readline

n, m, b = map(int, input().split())
ground = {}
for _ in range(n):
    for num in list(map(int, input().split())):
        if num in ground:
            ground[num] += 1
        else:
            ground[num] = 1
time = 0
max_n = max(ground.keys())
max_cnt = ground[max_n]
min_n = min(ground.keys())
min_cnt = ground[min_n]

while 1:
    if min_n == max_n:
        break

    if max_cnt*2 >= min_cnt and b >= min_cnt:
        b -= min_cnt
        time += min_cnt
        min_n += 1
        if min_n in ground:
            min_cnt += ground[min_n]
    else:
        b += max_cnt
        time += max_cnt * 2
        max_n -= 1
        if max_n in ground:
            max_cnt += ground[max_n]

print(time, min_n)