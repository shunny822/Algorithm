import sys
input = sys.stdin.readline

def opposite(store):
    d, i = store
    if d in {1, 2}:
        return min((i + me[1] + h), ((w-i) + (w-me[1]) + h))
    else:
        return min((i + me[1] + w), ((w-i) + (w-me[1]) + w))

def near(store):
    d, i = store
    if {d, me[0]} == {1, 3}:
        return i + me[1]
    elif {d, me[0]} == {1, 4}:
        if d == 1:
            return w - i + me[1]
        else:
            return w - me[1] + i
    elif {d, me[0]} == {2, 3}:
        if d == 2:
            return i + h - me[1]
        else:
            return me[1] + h - i
    elif {d, me[0]} == {2, 4}:
        return w + h - i - me[1]


w, h = map(int, input().split())
n = int(input())
stores = [tuple(map(int, input().split())) for _ in range(n)]
me = tuple(map(int, input().split()))

ans = 0
for dir, index in stores:
    if dir == me[0]:
        ans += abs(index - me[1])
    else:
        if (dir in {1, 2} and me[0] in {1, 2}) or (dir in {3, 4} and me[0] in {3, 4}):
            ans += opposite((dir, index))
        else:
            ans += near((dir, index))

print(ans)