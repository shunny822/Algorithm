import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b):
    check[a] = True
    q = deque([(a, 0)])

    while q:
        now, cnt = q.popleft()
        for member in members[now]:
            if member == b:
                score[a] = max(score[a], cnt + 1)
                score[b] = max(score[b], cnt + 1)
                return

            if not check[member]:
                check[member] = True
                q.append((member, cnt + 1))

n = int(input())
members = [[] for _ in range(n+1)]

while 1:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    members[a].append(b)
    members[b].append(a)

score = [0] * (n+1)
score[0] = 50
for i in range(1, n):
    for j in range(i+1, n+1):
        check = [False] * (n+1)
        bfs(i, j)

ans = min(score)
print(ans, score.count(ans))
for i, s in enumerate(score):
    if s == ans:
        print(i, end=' ')