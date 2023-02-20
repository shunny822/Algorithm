import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b):
    q = deque([a])
    check[a] = True
    cnt = {a: 0}

    while q:
        x = q.popleft()
        for friend in friends[x]:
            if friend == b:
                friends_cnt[a] += cnt[x] + 1
                friends_cnt[b] += cnt[x] + 1
                return
            elif not check[friend]:
                check[friend] = True
                q.append(friend)
                cnt[friend] = cnt[x] + 1

n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
friends_cnt = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(1, n):
    for j in range(i+1, n+1):
        check = [False] * (n+1)
        bfs(i, j)

friends_cnt[0] = n * n
print(friends_cnt.index(min(friends_cnt)))