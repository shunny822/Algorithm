import sys
input = sys.stdin.readline

def cut(start, end):
    mid_h = (end + start) // 2
    mid = 0
    for tree in trees:
        if tree > mid_h:
            mid += tree - mid_h
    
    if mid == m or start == mid_h:
        return print(mid_h)
    elif mid < m:
        cut(start, mid_h)
    else:
        cut(mid_h, end)
    
n, m = map(int, input().split())
trees = list(map(int, input().split()))
cut(0, max(trees))