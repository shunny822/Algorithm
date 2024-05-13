import sys
input = sys.stdin.readline

def floyd():
    for i in range(1, n+1):
        cost[i][i] = 0
    
    for mid in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                cost[s][e] = min(cost[s][e], cost[s][mid] + cost[mid][e])


n = int(input())
m = int(input())
cost = [[1e9] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

floyd()

for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == 1e9:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
        
    print()