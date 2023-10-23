import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
picture = []
for _ in range(r):
    px = list(map(int, input().split()))
    cnt = 0
    line = []
    for i in range(c):
        cnt += px[i]
        line.append(cnt)
    picture.append(line)

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    avg = 0
    for i in range(r1-1, r2):
        if c1 == 1:
            avg += picture[i][c2-1]
        else:
            avg += picture[i][c2-1] - picture[i][c1-2]
    print(avg//((r2-r1+1)*(c2-c1+1)))