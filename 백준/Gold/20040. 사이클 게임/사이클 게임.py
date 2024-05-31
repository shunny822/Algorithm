import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n)]
cnt = 1

for _ in range(m):
    s, e = map(int, input().split())
    
    if find(s) == find(e):
        print(cnt)
        break

    union(s, e)
    cnt += 1
else:
    print(0)