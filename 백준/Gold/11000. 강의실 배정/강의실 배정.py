import sys
input = sys.stdin.readline
import heapq

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()
classes = [time[0][1]]

for i in range(1, n):
    s, e = time[i]
    if classes[0] > s:
        heapq.heappush(classes, e)
    else:
        heapq.heapreplace(classes, e)

print(len(classes))