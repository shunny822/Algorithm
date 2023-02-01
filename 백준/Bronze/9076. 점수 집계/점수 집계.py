import sys

t = int(input())
for _ in range(t):
    score = list(map(int, sys.stdin.readline().split()))
    score = sorted(score)[1:4]
    print(sum(score) if score[2] - score[0] < 4 else 'KIN')