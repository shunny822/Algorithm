import sys
input = sys.stdin.readline
import heapq

n = int(input())
array = list(map(int, input().split()))
heapq.heapify(array)

for _ in range(n-1):
    line = list(map(int, input().split()))
    for l in line:
        heapq.heappushpop(array, l)

print(array[0])
