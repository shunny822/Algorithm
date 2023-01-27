import sys
import heapq

l = []
heapq.heapify(l)

n = int(input())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if l:
            print(l[0][1])
            heapq.heappop(l)
        else:
            print(0)
    else:
        heapq.heappush(l, (abs(x), x))