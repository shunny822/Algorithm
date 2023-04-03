import sys
input = sys.stdin.readline

n = int(input())
pillar = [tuple(map(int, input().split())) for _ in range(n)]
pillar.sort(key=lambda x: x[1], reverse=True)
total = pillar[0][1]
flag = left_f = right_f = pillar[0][0]

for i in range(1, n):
    x, y = pillar[i]
    if x < flag and x < left_f:
        total += (left_f - x) * y
        left_f = x
    elif x > flag and x > right_f:
        total += (x - right_f) * y
        right_f = x

print(total)