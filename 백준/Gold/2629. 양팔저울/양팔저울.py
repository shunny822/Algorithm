import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
m = int(input())
balls = list(map(int, input().split()))
dp = [[0] * (40001) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 40001):
        if j == w[i-1]:
            dp[i][j] = 1

        if dp[i-1][j] == 1:
            dp[i][j] = 1

            if w[i-1] + j < 40001:
                dp[i][w[i-1]+j] = 1
            dp[i][abs(w[i-1]-j)] = 1
            dp[i][abs(j-w[i-1])] = 1

ans = []

for ball in balls:
    if dp[-1][ball]:
        ans.append('Y')
    else:
        ans.append('N')

print(' '.join(ans))