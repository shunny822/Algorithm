import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))
cnt = 0
stack = []

for i, l in enumerate(block):
    while stack and block[stack[-1]] < l:
        little = block[stack.pop()]
        if not stack:
            break
        d = i - stack[-1] - 1
        wh = min(block[stack[-1]], l) - little
        cnt += d * wh
    stack.append(i)

print(cnt)