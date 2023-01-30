import sys

score = [sum(map(int, sys.stdin.readline().split())) for _ in range(5)]
win = max(score)
for i, s in enumerate(score):
    if s == win:
        print(i+1, win)