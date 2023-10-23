import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
picture = [[0] * (c+1)]
for i in range(r):
    picture.append([0] + list(map(int, input().split())))

for i in range(1, r+1):
    for j in range(1, c+1):
        picture[i][j] += picture[i-1][j] + picture[i][j-1] - picture[i-1][j-1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    print((picture[r2][c2] - picture[r2][c1-1] - picture[r1-1][c2] + picture[r1-1][c1-1])//((r2-r1+1)*(c2-c1+1)))