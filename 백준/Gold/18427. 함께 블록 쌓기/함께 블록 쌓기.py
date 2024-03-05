import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (h+1) for _ in range(n+1)]

for i in range(1, n+1):
    for x in range(1, h+1):
        dp[i][x] = dp[i-1][x]

        for block in blocks[i-1]:
            if block == x:
                dp[i][x] += 1
            elif block < x and dp[i-1][x-block] > 0:
                dp[i][x] += dp[i-1][x-block]

print(dp[-1][-1] % 10007)