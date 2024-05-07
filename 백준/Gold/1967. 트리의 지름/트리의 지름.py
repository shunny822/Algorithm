import sys
input = sys.stdin.readline

def dfs(start):
    check = [False] * (n+1)
    check[start] = True
    stack = [(start, 0)]
    res = 0
    node = 0

    while stack:
        now, dist = stack.pop()
        
        if dist > res:
            res = dist
            node = now

        for next, d in nodes[now]:
            if not check[next]:
                check[next] = True
                stack.append((next, dist+d))
    
    return res, node


n = int(input())
nodes = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, v = map(int, input().split())
    nodes[p].append((c, v))
    nodes[c].append((p, v))

ans, node1 = dfs(1)
ans, node2 = dfs(node1)

print(ans)