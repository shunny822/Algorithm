import sys
input = sys.stdin.readline

n, l = map(int, input().split())
signals = [tuple(map(int, input().split())) for _ in range(n)]
signals.append((l, 0, 0))
time = signals[0][0]

for i in range(n):
    d, r, g = signals[i]
    diff = signals[i+1][0] - d
    x = time % (r+g)
    if x < r:
        time += r - x
    time += diff

print(time)