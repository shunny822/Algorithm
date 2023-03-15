import sys
input = sys.stdin.readline

n, c, w = map(int, input().split())
length = [int(input()) for _ in range(n)]
max_money = 0

for x in range(1, max(length)+1):
    money = 0
    for l in length:
        d, m = divmod(l, x)
        if m == 0:
            if x*d*w - c*(d-1) > 0:
                money += x*d*w - c*(d-1)
        else:
            if x*d*w - c*d > 0:
                money += x*d*w - c*d

    if money > max_money:
        max_money = money

print(max_money)