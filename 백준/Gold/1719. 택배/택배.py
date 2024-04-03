import sys
input = sys.stdin.readline
import heapq

def dikjstra(time, start):
    q = []
    time[start] = (0, '-')

    for node, sec in graph[start]:
        heapq.heappush(q, (sec, node, node))
        time[node] = (sec, node)
    
    while q:
        sec, now, flag = heapq.heappop(q)

        if sec > time[now][0]:
            continue

        for next, s in graph[now]:
            temp = sec + s

            if temp < time[next][0]:
                heapq.heappush(q, (temp, next, flag))
                time[next] = (temp, flag)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, s = map(int, input().split())
    graph[a].append((b, s))
    graph[b].append((a, s))

for i in range(1, n+1):
    time = [(1e9, 0)] * (n+1)
    dikjstra(time, i)

    res = ''

    for j in range(1, n+1):
        res += f'{str(time[j][1])} '
    
    print(res.rstrip())