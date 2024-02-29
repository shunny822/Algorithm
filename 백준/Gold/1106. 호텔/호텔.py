import sys
input = sys.stdin.readline

C, N = map(int,input().split())
cost_list = [tuple(map(int,input().split())) for _ in range(N)]
dp = [1e9 for _ in range(C+100)]
dp[0] = 0

for cost, num in cost_list:
    for i in range(num, C+100):
        dp[i] = min(dp[i-num] + cost, dp[i])
 
print(min(dp[C:]))