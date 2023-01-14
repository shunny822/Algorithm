import sys

t = int(input())
for i in range(t):
    score = list(map(int, sys.stdin.readline().split()))
    aver = sum(score[1:])/score[0]
    cnt = 0
    for j in score[1:]:
        if j > aver:
            cnt += 1
    rate = format(cnt/score[0]*100, '.3f')
    print(f'{rate}%')