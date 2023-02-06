import sys

def dfs(start):
    stack = [start]
    check[start] = 1
    while stack:
        cur = stack.pop()
        for adj in com[cur]:
            if check[adj] == 0:
                check[adj] = 1
                stack.append(adj)
    return sum(check)

n = int(input())
check = [0]*(n+1)
com = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    com[a].append(b)
    com[b].append(a)

print(dfs(1)-1)