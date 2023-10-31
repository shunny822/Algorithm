import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]
belt += belt
sushi = {c: 1}

for i in range(k):
    sushi[belt[i]] = sushi.get(belt[i], 0) + 1

res = len(sushi)
s = 0
e = k - 1
for i in range(n):
    e += 1
    sushi[belt[e]] = sushi.get(belt[e], 0) + 1
    if sushi[belt[s]] == 1:
        sushi.pop(belt[s])
    else:
        sushi[belt[s]] -= 1
    s += 1
    res = max(res, len(sushi))

print(res)