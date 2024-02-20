import sys
input = sys.stdin.readline
import heapq

def dijkstra(start, dist):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)

        if d > dist[now]:
            continue

        for next, next_cost in graph[now]:
            cost = d + next_cost

            if cost < dist[next]:
                heapq.heappush(q, (cost, next))
                dist[next] = cost

n, m, x = map(int, input().split())
students = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, n+1):
    distance = [1e9] * (n + 1)
    dijkstra(i, distance)
    students[i] = distance[x]

distance = [1e9] * (n + 1)
dijkstra(x, distance)

for i in range(1, n+1):
    students[i] += distance[i]

print(max(students))