import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
home = []
store = []

for i in range(n):
    line = list(map(int, input().split()))
    for j, num in enumerate(line):
        if num == 1:
            home.append((i, j))
        elif num == 2:
            store.append((i, j))

ans = 1e9
for picks in combinations(store, m):
    temp = 0
    for y, x in home:
        temp += min([abs(yy-y) + abs(xx-x) for yy, xx in picks])
    ans = min(ans, temp)

print(ans)