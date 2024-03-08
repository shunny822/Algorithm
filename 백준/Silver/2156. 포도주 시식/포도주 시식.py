import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(wine))
elif n == 3:
    print(sum(wine) - min(wine))
else:
    dp = [0] * n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])

    for i in range(3, n):
        dp[i] = max(dp[i-1], wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2])
    
    print(dp[-1])