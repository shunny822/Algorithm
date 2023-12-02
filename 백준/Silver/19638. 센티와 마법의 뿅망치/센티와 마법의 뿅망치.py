import sys
input = sys.stdin.readline
import heapq

n, h, t = map(int, input().split())
people =[-1 * int(input()) for _ in range(n)]
heapq.heapify(people)
cnt = 0

while cnt < t:
    if abs(people[0]) < h:
        break

    if abs(people[0]) > 1:
        p = heapq.heappop(people)
        heapq.heappush(people, -1 * (abs(p)//2))
    cnt += 1

if abs(people[0]) < h:
    print('YES')
    print(cnt)
else:
    print('NO')
    print(abs(people[0]))