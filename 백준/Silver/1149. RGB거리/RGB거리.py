import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * 3 for _ in range(n)]

memo[0] = cost[0]

for i in range(1, n):
    memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + cost[i][0]
    memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + cost[i][1]
    memo[i][2] = min(memo[i-1][0], memo[i-1][1]) + cost[i][2]

print(min(memo[-1]))