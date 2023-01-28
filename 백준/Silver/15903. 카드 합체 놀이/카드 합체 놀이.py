import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)
for _ in range(m):
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    heapq.heappush(card, x+y)
    heapq.heappush(card, x+y)

print(sum(card))