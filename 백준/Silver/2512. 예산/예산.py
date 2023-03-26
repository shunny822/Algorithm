import sys
input = sys.stdin.readline

n = int(input())
wish = list(map(int, input().split()))
budget = int(input())
s = 1
e = max(wish)
m = 0

while s <= e:
    m = (s + e) // 2
    total = 0
    for w in wish:
        if w <= m:
            total += w
        else:
            total += m
    
    if total <= budget:
        s = m + 1
    else:
        e = m - 1

print(max(wish) if sum(wish) <= budget else e)