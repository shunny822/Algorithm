import sys
input = sys.stdin.readline
import itertools

n = int(input())
tastes = [tuple(map(int, input().split())) for _ in range(n)]
result = 2e9

for i in range(1, n+1):
    for combis in itertools.combinations(tastes, i):
        sour = 1
        bitter = 0
        for combi in combis:
            s, b = combi
            sour *= s
            bitter += b
        if abs(sour - bitter) < result:
            result = abs(sour - bitter)

print(result)