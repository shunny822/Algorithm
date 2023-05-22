import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    max_n = 0
    res = 0
    for p in reversed(price):
        if p > max_n:
            max_n = p
        else:
            res += max_n - p
    print(res)