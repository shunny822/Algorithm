import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, d in graph[now]:
            temp = dist + d

            if temp < distance[next]:
                distance[next] = temp
                heapq.heappush(q, (temp, next))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())

dijkstra(s)
print(distance[t])