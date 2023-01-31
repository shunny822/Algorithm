import sys

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    turn_matrix = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            turn_matrix[i][j] = matrix[j][i]

    total = 0
    for i in range(n):
        cnt = 0
        for j in range(-1,-(m+1),-1):
            if turn_matrix[i][j]:
                total += cnt
            else:
                cnt += 1

    print(total)