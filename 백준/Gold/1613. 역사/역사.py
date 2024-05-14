import sys
input = sys.stdin.readline

def floyd():    
    for mid in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                if seq[s][mid] and seq[mid][e]:
                    seq[s][e] = 1


n, k = map(int, input().split())
seq = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    seq[a][b] = 1

floyd()

s = int(input())

for _ in range(s):
    a, b = map(int, input().split())
    
    if seq[a][b]:
        print(-1)
    elif seq[b][a]:
        print(1)
    else:
        print(0)