import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    cost[start] = 0

    while q:
        total, now = heapq.heappop(q)

        if cost[now] < total:
            continue

        for next, d in graph[now]:
            temp = total + d

            if temp < cost[next]:
                heapq.heappush(q, (temp, next))
                cost[next] = temp

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
cost = [1e9] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())

dijkstra(s)
print(cost[e])