import sys
input = sys.stdin.readline

N, L = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()
cnt = 1
tape = 1

for i in range(1, N):
    tape += hole[i] - hole[i-1]
    if tape > L:
        cnt += 1
        tape = 1

print(cnt)