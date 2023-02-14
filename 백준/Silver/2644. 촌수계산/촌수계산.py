import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(n, cnt, result):
    check[n] = True
    cnt += 1

    for num in family[n]:
        if num == y:
            result = cnt
            return result
        elif not check[num]:
            result = dfs(num, cnt, result)

    return result

n = int(input())
family = [[] for _ in range(n+1)]
check = [False] * (n+1)
x, y = map(int, input().split())
k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)

print(dfs(x, 0, -1))