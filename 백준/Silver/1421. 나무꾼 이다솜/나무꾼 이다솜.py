import sys
input = sys.stdin.readline

n, c, w = map(int, input().split())
length = sorted([int(input()) for _ in range(n)])
max_money = length[-1] * w

if n == 1:
    print(max_money)
else:
    for x in range(1, length[-2]+1):
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