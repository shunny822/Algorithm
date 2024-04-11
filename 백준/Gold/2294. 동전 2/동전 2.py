import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = set([int(input()) for _ in range(n)])
dp = [1e9] * (k+1)

for c in coin:
    for i in range(1, k+1):
        if c > i:
            continue

        if c == i:
            dp[i] = 1
        else:
            if dp[i] != 1e9 and dp[i-c] != 1e9:
                dp[i] = min(dp[i], dp[i-c] + 1)
            elif dp[i-c] != 1e9:
                dp[i] = dp[i-c] + 1

if dp[-1] == 1e9:
    print(-1)
else:
    print(dp[-1])