import sys
intput = sys.stdin.readline

n = int(input())
p = sorted(list(map(int, input().split())))
result = 0
t = 0
for i in range(n):
    t += p[i]
    result += t
print(result)