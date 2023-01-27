import sys

input = sys.stdin.readline
n, m = map(int, input().split())
s = {input().rstrip() for _ in range(n)}
cnt = 0
for _ in range(m):
    if input().rstrip() in s:
        cnt += 1
print(cnt)