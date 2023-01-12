t = int(input())
score = list(map(int, input().split()))
best = max(score)
for i, s in enumerate(score):
    score[i] = s/best*100
print(sum(score)/t)