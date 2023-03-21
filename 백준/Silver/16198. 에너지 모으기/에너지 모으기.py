import sys
input = sys.stdin.readline
import itertools

n = int(input())
balls = list(map(int, input().split()))
result = 0

for combi in itertools.permutations(range(1, n-1), n-2):
    is_used = [False] * n
    total = 0

    for i in combi:
        is_used[i] = True
        a = b = i
        while is_used[a]:
            a -= 1
        while is_used[b]:
            b += 1
        total += balls[a] * balls[b]
    
    if total > result:
        result = total

print(result)