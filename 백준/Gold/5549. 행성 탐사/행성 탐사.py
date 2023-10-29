import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())
planet = [[[0, 0, 0] for _ in range(n+1)]]
planet += [[[0, 0, 0] for _ in range(n+1)] for _ in range(m+1)]

for i in range(m):
    line = input().rstrip()
    for j in range(n):
        if line[j] == 'J':
            planet[i+1][j+1][0] = 1
        elif line[j] == 'O':
            planet[i+1][j+1][1] = 1
        else:
            planet[i+1][j+1][2] = 1

for y in range(1, m+1):
    for x in range(1, n+1):
        planet[y][x][0] += planet[y-1][x][0] + planet[y][x-1][0] - planet[y-1][x-1][0]
        planet[y][x][1] += planet[y-1][x][1] + planet[y][x-1][1] - planet[y-1][x-1][1]
        planet[y][x][2] += planet[y-1][x][2] + planet[y][x-1][2] - planet[y-1][x-1][2]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    j, o, i = planet[c][d]
    j = j - planet[c][b-1][0] - planet[a-1][d][0] + planet[a-1][b-1][0]
    o = o - planet[c][b-1][1] - planet[a-1][d][1] + planet[a-1][b-1][1]
    i = i - planet[c][b-1][2] - planet[a-1][d][2] + planet[a-1][b-1][2]
    print(j, o, i)
