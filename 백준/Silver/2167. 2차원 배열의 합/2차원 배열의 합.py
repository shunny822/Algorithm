import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
for _ in range(k):
    total = 0
    i, j, x, y = map(int, input().split())

    for a in range(i-1, x):
        for b in range(j-1, y):
            total += matrix[a][b]

    print(total)