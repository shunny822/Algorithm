import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = {i: int(v) for i, v in enumerate(input().split())}
blocks = sorted(heights.items(), key=lambda x: x[1], reverse=True)
cnt = 0
center = left = right = blocks[0][0]

for i, v in blocks:
    if i < left:
        for j in range(i+1, left):
            cnt += v - heights[j]
        left = i
    elif i > right:
        for j in range(right+1, i):
            cnt += v - heights[j]
        right = i

print(cnt)