import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
stack = [seq[-1]]
res = [-1]

for s in reversed(seq[:n-1]):
    while stack and stack[-1] <= s:
        stack.pop()
    
    if stack:
        res.append(stack[-1])
    else:
        res.append(-1)
    
    stack.append(s)

print(*res[::-1])