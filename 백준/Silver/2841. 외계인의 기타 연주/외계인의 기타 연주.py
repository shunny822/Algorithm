import sys
input = sys.stdin.readline

n, _ = map(int, input().split())
guitar = [[] for _ in range(7)]

cnt = 0
for _ in range(n):
    l, p = map(int, input().split())

    while guitar[l] and guitar[l][-1] > p:
        guitar[l].pop()
        cnt += 1
    
    if guitar[l] and guitar[l][-1] == p:
        continue
    else:
        guitar[l].append(p)
        cnt += 1

print(cnt)