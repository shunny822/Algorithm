import sys
intput = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
total = 0
for i in range(n):
    total += a[i] * b[i]
print(total)