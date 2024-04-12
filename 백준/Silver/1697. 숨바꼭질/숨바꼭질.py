import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n, k = map(int, input().split())

    if n >= k:
        return n - k
    
    sec = 0
    q = deque([(sec, n)])
    check = [False] * 100001

    while q:
        s, x = q.popleft()

        if x == k:
            return s

        for next in [x-1, x+1, x*2]:
            if 0 <= next <= 100000 and not check[next]:
                check[next] = True
                q.append((s+1, next))

print(solve())