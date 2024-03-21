import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)

for coin in coins:
    for i in range(1, k+1):
        if coin < i:
            dp[i] += dp[i-coin]
        elif coin == i:
            dp[i] += 1

print(dp[-1])