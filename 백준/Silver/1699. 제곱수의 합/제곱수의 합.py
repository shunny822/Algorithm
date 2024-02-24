import sys
input = sys.stdin.readline

n = int(input())

if n <= 3:
    print(n)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4, n+1):
        x = int(i**(1/2))

        if x**2 == i:
            dp[i] = 1
        else:
            dp[i] = min([dp[j**2] + dp[i - j**2] for j in range(1, x+1)])
    
    print(dp[n])