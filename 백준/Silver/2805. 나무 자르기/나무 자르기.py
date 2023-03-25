import sys
input = sys.stdin.readline

def cut(start, end):
    mid_h = (end + start) // 2
    mid = 0
    for tree, num in trees.items():
        if tree > mid_h:
            mid += (tree - mid_h) * num
    
    if start > end:
        return print(mid_h)
    elif mid < m:
        cut(start, mid_h-1)
    else:
        cut(mid_h+1, end)

n, m = map(int, input().split())
trees = {}
for h in map(int, input().split()):
    trees[h] = trees.get(h, 0) + 1

cut(0, max(trees))