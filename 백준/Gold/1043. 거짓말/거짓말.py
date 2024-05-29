import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a in truth and b in truth:
        return
    
    if a in truth:
        parent[b] = a
    elif b in truth:
        parent[a] = b
    else:
        res = min(a, b)
        parent[a] = res
        parent[b] = res


n, m = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])
party = []
parent = [i for i in range(n+1)]

for _ in range(m):
    people = list(map(int, input().split()))
    party.append(people[1:])

    for i in range(1, people[0]):
        union(people[i], people[i+1])

cnt = 0

for p in party:
    for person in p:
        if find(parent[person]) in truth:
            break
    else:
        cnt += 1

print(cnt)