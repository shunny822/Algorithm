import sys
input = sys.stdin.readline
import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    min_heapq = []
    max_heapq = []
    cnt = {}

    for _ in range(k):
        order, number = input().rstrip().split()
        number = int(number)

        if order == 'I':
            heapq.heappush(min_heapq, number)
            heapq.heappush(max_heapq, -number)
            cnt[number] = cnt.get(number, 0) + 1
        else:
            x = 1e9
            if number == -1:
                while min_heapq and min_heapq[0] not in cnt:
                    heapq.heappop(min_heapq)
                
                if min_heapq:
                    x = heapq.heappop(min_heapq)

            elif number == 1:
                while max_heapq and -max_heapq[0] not in cnt:
                    heapq.heappop(max_heapq)
                
                if max_heapq:
                    x = -heapq.heappop(max_heapq)
            
            if x != 1e9:
                if cnt[x] == 1:
                    cnt.pop(x)
                else:
                    cnt[x] -= 1
    
    if cnt:
        while min_heapq[0] not in cnt:
            heapq.heappop(min_heapq)
        
        while -max_heapq[0] not in cnt:
            heapq.heappop(max_heapq)

        print(-max_heapq[0], min_heapq[0])
    else:
        print('EMPTY')