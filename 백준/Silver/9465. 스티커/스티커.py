import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stickers = [[0] + list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(stickers[0][1], stickers[1][1]))
    elif n == 2:
        print(max(stickers[1][1] + stickers[0][2], stickers[0][1] + stickers[1][2]))
    else:
        dp = [[0] * (n + 1) for _ in range(2)]
        dp[0][1], dp[1][1] = stickers[0][1], stickers[1][1]
        dp[0][2], dp[1][2] = dp[1][1] + stickers[0][2], dp[0][1] + stickers[1][2]

        for i in range(3, n+1):
            dp[0][i] = max(dp[1][i-2] + stickers[0][i], dp[1][i-1] + stickers[0][i])
            dp[1][i] = max(dp[0][i-2] + stickers[1][i], dp[0][i-1] + stickers[1][i])
        
        print(max(dp[0][-1], dp[1][-1]))