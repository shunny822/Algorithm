import sys
input = sys.stdin.readline
import heapq

def dikjstra(graph, time, start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0

    while q:
        sec, now = heapq.heappop(q)

        if sec > time[now]:
            continue

        for next, s in graph[now]:
            temp = sec + s

            if temp < time[next]:
                time[next] = temp
                heapq.heappush(q, (temp, next))


t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    time = [1e9] * (n+1)

    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    dikjstra(graph, time, c)

    cnt = 0
    last_sec = 0

    for sec in time:
        if sec < 1e9:
            cnt += 1
            last_sec = max(last_sec, sec)
    
    print(cnt, last_sec)