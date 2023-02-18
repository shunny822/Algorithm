import sys
input = sys.stdin.readline
from collections import deque

def dfs(x):
    print(x, end=' ')
    check[x] = True
    
    for i in sorted(l[x]):
        if not check[i]:
            dfs(i)
    return

def bfs(x):
    print(x, end=' ')
    check[x] = True
    q = deque([x])

    while q:
        num = q.popleft()
        for i in sorted(l[num]):
            if not check[i]:
                q.append(i)
                check[i] = True
                print(i, end=' ')

n, m, v = map(int, input().split())
l = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

check = [False] * (n+1)
dfs(v)
print()
check = [False] * (n+1)
bfs(v)