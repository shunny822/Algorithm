import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
distance = [1e9 for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, k))
distance[k] = 0

while q:
    d, node = heapq.heappop(q)

    if distance[node] < d:
        continue

    for nn, nd in graph[node]:
        cost = d + nd
        if cost < distance[nn]:
            distance[nn] = cost
            heapq.heappush(q, (cost, nn))

for d in distance[1:]:
    if d == 1e9:
        print('INF')
    else:
        print(d)