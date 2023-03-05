import sys
intput = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
oil = list(map(int, input().split()))
price = oil[0]
total = 0

for i in range(n-1):
    total += d[i] * price
    if oil[i+1] < price:
        price = oil[i+1]

print(total)