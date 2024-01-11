import sys

s = int(input())
n = cnt = 0
a = 1

while n + a <= s:
    n += a
    cnt += 1
    a += 1

print(cnt)