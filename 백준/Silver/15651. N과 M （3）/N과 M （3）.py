import itertools

n, m = map(int, input().split())
for combi in itertools.product(range(1, n+1), repeat=m):
    print(*combi)