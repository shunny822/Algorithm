import sys
import heapq

w = []
k = []
for i in range(10):
    if i < 3:
        heapq.heappush(w, int(sys.stdin.readline()))
    else:
        heapq.heappushpop(w, int(sys.stdin.readline()))

for i in range(10):
    if i < 3:
        heapq.heappush(k, int(sys.stdin.readline()))
    else:
        heapq.heappushpop(k, int(sys.stdin.readline()))

print(sum(w), sum(k))