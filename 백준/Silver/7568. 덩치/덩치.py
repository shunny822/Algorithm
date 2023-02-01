import sys

n = int(input())
data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
rank = [1]*n
for i in range(n-1):
    for j in range(i+1,n):
        if data[i][0] > data[j][0] and data[i][1] > data[j][1]:
            rank[j] += 1
        elif data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank[i] += 1
print(*rank)