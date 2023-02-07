import sys

n = int(input())
sticks = [int(sys.stdin.readline()) for _ in range(n)]
long = sticks[-1]
cnt = 1
for i in reversed(range(n)):
    if sticks[i] > long:
        long = sticks[i]
        cnt += 1
print(cnt)