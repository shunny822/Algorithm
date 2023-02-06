import sys

train = answer = 0
for _ in range(4):
    a, b = map(int, input().split())
    train += b-a
    if train > answer:
        answer = train
print(answer)