import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    max_price = price[-1]
    profit = 0

    for i in reversed(range(n)):
        if price[i] > max_price:
            max_price = price[i]
        else:
            profit += max_price - price[i]
    
    print(profit)