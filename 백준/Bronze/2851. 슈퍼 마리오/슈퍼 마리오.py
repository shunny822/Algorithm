import sys

mush = [int(sys.stdin.readline()) for _ in range(10)]
score = []
total = 0

for s in mush:
    total += s
    score.append(total)
    if total >= 100:
        break

if score[-1] == 100 and len(score) == 1:
    print(score[-1])
elif abs(score[-1] - 100) <= abs(score[-2] - 100):
    print(score[-1])
else:
    print(score[-2])