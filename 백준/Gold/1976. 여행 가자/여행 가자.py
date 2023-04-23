import sys
input = sys.stdin.readline

def dfs(start, end, visited):
    stack = [start]
    visited[start] = True

    while stack:
        x = stack.pop()
        if x == end:
            return True
        for j in range(n):
            if matrix[x][j] and not visited[j]:
                stack.append(j)
                visited[j] = True
    return False

n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
route = list(map(int, input().split()))

for i in range(m-1):
    check = [False] * n
    is_possible = dfs(route[i]-1, route[i+1]-1, check)
    if not is_possible:
        print('NO')
        break
else:
    print('YES')