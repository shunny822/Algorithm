import sys
input = sys.stdin.readline

def team_maker(check, s):
    if sum(check) == n//2:
        team_a = [i for i in range(n) if check[i]]
        team_b = [i for i in range(n) if not check[i]]
        a = b = 0

        for i in team_a:
            for j in team_a:
                a += stat[i][j]
        for i in team_b:
            for j in team_b:
                b += stat[i][j]

        result.append(abs(a - b))
        return

    for i in range(s, n):
        if not check[i]:
            check[i] = True
            team_maker(check, i+1)
            check[i] = False

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
is_used = [False] * n
result = []
team_maker(is_used, 0)
print(min(result))