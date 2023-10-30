import sys
input = sys.stdin.readline

n = int(input())
top = []
cnt = 0

for _ in range(n):
    cnt += int(input())
    top.append(cnt)

res = 0
s = 0
e = 1
while s < e and e < n:
    right = top[e] - top[s]
    left = cnt - right
    
    if right > left:
        s += 1
        res = max(res, left)
    else:
        e += 1
        res = max(res, right)

print(res)