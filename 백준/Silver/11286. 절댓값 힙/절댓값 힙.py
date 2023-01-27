import sys
input = sys.stdin.readline
import heapq

n = int(input())
array = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(array, (abs(x), x))
    else:
        if array:
            print(array[0][1])
            heapq.heappop(array)
        else:
            print(0)