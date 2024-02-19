import sys
input = sys.stdin.readline
import heapq

def dijkstra(cave, costs):
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))
    costs[0][0] = cave[0][0]

    while q:
        cost, y, x = heapq.heappop(q)

        if cost > costs[y][x]:
            continue

        for dy, dx in delta:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < n:
                temp_cost = cost + cave[ny][nx]

                if temp_cost < costs[ny][nx]:
                    heapq.heappush(q, (temp_cost, ny, nx))
                    costs[ny][nx] = temp_cost

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
turn = 1

while 1:
    n = int(input())

    if n == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(n)]
    costs = [[1e9] * n for _ in range(n)]

    dijkstra(cave, costs)
    print(f'Problem {turn}: {costs[n-1][n-1]}')
    turn += 1