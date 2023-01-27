import sys
input = sys.stdin.readline
import heapq

n = int(input())
array = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(array, -x)
    else:
        print(-(heapq.heappop(array) if array else 0))