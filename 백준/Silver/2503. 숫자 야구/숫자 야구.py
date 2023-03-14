import sys
input = sys.stdin.readline
import itertools

def throw_ball(num, target):
    strike = 0
    ball = 0
    for i in range(3):
        if num[i] == target[i]:
            strike += 1
        elif num[i] in target:
            ball += 1
    return (strike, ball)

n = int(input())
answer = [tuple(map(int, input().split())) for _ in range(n)]
cnt = 0

for number in itertools.permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3):
    for t, s, b in answer:
        if (s, b) != throw_ball(number, str(t)):
            break
    else:
        cnt += 1
print(cnt)