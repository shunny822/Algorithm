import sys
input = sys.stdin.readline
import itertools

n, m = map(int, input().split())
house = []
store = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            house.append((i, j))
        elif line[j] == 2:
            store.append((i, j))

result = 1e9
for combi in itertools.combinations(store, m):
    total = 0
    for r, c in house:
        total += min([abs(r-y) + abs(c-x) for y, x in combi])

    if total < result:
        result = total

print(result)