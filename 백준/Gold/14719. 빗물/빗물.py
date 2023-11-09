import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))
rain = 0
stack = []

for i, l in enumerate(block):
    while stack and block[stack[-1]] < l:
        little_i = stack.pop()
        if not stack:
            break
        d = i - stack[-1] - 1
        rain += (min(block[stack[-1]], l) - block[little_i]) * d

    stack.append(i)

print(rain)