import sys
input = sys.stdin.readline

c, r = map(int, input().split())
k = int(input())
x = 1
y = 0

if k > c * r:
    print(0)
else:
    c -= 1
    while 1:
        if k - r <= 0:
            y += k
            break
        else:
            k -= r
            y += r
            r -= 1
        if k - c <= 0:
            x += k
            break
        else:
            k -= c
            x += c
            c -= 1
        if k - r <= 0:
            y -= k
            break
        else:
            k -= r
            y -= r
            r -= 1
        if k - c <= 0:
            x -= k
            break
        else:
            k -= c
            x -= c
            c -= 1
    print(x, y)