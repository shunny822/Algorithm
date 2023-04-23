import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, end, visited):
    q = deque([start])
    visited[start] = True

    while q:
        x = q.popleft()
        if x == end:
            return True
        for j in range(n):
            if matrix[x][j] and not visited[j]:
                q.append(j)
                visited[j] = True
    return False


n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
route = list(map(int, input().split()))

for i in range(m-1):
    check = [False] * n
    is_possible = bfs(route[i]-1, route[i+1]-1, check)
    if not is_possible:
        print('NO')
        break
else:
    print('YES')