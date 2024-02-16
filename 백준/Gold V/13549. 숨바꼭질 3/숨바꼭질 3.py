import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[n] = 0

    while q:
        turn, node = heapq.heappop(q)

        if distance[node] < turn:
            continue

        for i, next in enumerate([node * 2, node + 1, node - 1]):
            nt = turn if i == 0 else turn + 1

            if next < 0 or next >= MAX:
                continue
        
            if nt < distance[next]:
                distance[next] = nt
                heapq.heappush(q, (nt, next))


n, k = map(int, input().split())
MAX = 100001
distance = [1e9] * MAX

dijkstra(n)
print(distance[k])