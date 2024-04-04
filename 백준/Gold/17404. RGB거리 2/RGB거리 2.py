import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9

for i in range(3):
    dp = [[0, 0, 0] for _ in range(n)]
    
    for k in range(3):
        if i == k:
            dp[0][k] = house[0][k]
        else:
            dp[0][k] = 1e9

    for j in range(1, n):
        dp[j][0] = house[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = house[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = house[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i == j:
            continue

        ans = min(ans, dp[-1][j])

print(ans)