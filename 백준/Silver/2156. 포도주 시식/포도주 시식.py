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
    dp[2] = wine[2] + max(wine[0], wine[1])

    for i in range(3, n):
        dp[i] = wine[i] + max(dp[i-2], max(dp[:i-2]) + wine[i-1])
    
    print(max(dp[-1], dp[-2]))