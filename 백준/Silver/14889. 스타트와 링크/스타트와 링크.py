import sys
input = sys.stdin.readline
import itertools

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
total = set(range(n))
result = 1e9

for team_a in itertools.combinations(range(n), n//2):
    team_b = total - set(team_a)
    a = b = 0
    for i in team_a:
        for j in team_a:
            a += stat[i][j]
    for i in team_b:
        for j in team_b:
            b += stat[i][j]

    if abs(a - b) < result:
        result = abs(a - b)

print(result)