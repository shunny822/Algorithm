import sys
input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    tri[i][0] += tri[i-1][0]
    tri[i][-1] += tri[i-1][-1]
    
    for j in range(1, len(tri[i])-1):
        tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[-1]))