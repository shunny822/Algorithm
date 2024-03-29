import sys
input = sys.stdin.readline
import heapq

def dijkstra(count):
    q = []
    heapq.heappush(q, (0, 0, 0))
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        c, y, x = heapq.heappop(q)

        if count[y][x] < c:
            continue

        for dy, dx in delta:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < n:
                temp = c if room[ny][nx] else c + 1

                if temp < count[ny][nx]:
                    count[ny][nx] = temp
                    heapq.heappush(q, (temp, ny, nx))

    return count[-1][-1]


n = int(input())
room = [list(map(int, list(input().rstrip()))) for _ in range(n)]
cnt = [[1e9] * n for _ in range(n)]
cnt[0][0] = 0

print(dijkstra(cnt))