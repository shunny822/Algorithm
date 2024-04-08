import sys
input = sys.stdin.readline

n, S = map(int, input().split())
sequence = list(map(int, input().split()))
s = e = 0
cnt = sequence[0]
l = 1
res = 1e9

while s <= e:
    if cnt >= S:
        res = min(res, l)
        cnt -= sequence[s]
        l -= 1
        s += 1
    else:
        if e < n - 1:
            e += 1
            cnt += sequence[e]
            l += 1
        else:
            break

if res == 1e9:
    res = 0

print(res)