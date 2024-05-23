import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    x, y = find(a), find(b)

    if x < y:
        parent[y] = x
    elif y < x:
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    order, a, b = map(int, input().split())

    if order:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)