import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(1, k+1):
        if wv[i-1][0] > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], wv[i-1][1] + dp[i-1][w-wv[i-1][0]])

print(dp[n][k])