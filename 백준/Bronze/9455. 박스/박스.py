import sys

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    total = 0
    for i in range(n):
        cnt = 0
        for j in reversed(range(m)):
            if matrix[j][i]:
                total += cnt
            else:
                cnt += 1

    print(total)