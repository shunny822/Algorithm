import sys
import heapq

w = []
k = []
for i in range(10):
    if i < 3:
        heapq.heappush(w, int(sys.stdin.readline()))
    else:
        n = int(sys.stdin.readline())
        if n > w[0]:
            heapq.heapreplace(w, n)

for i in range(10):
    if i < 3:
        heapq.heappush(k, int(sys.stdin.readline()))
    else:
        n = int(sys.stdin.readline())
        if n > k[0]:
            heapq.heapreplace(k, n)

print(sum(w), sum(k))