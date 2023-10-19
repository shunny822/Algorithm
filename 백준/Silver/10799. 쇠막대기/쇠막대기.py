import sys
input = sys.stdin.readline

sticks = input().rstrip()
stack = []
cnt = 0
i = 0

while i < len(sticks)-1:
# for i in range(len(sticks)):
    if sticks[i] == '(' and sticks[i+1] == ')':
        cnt += len(stack)
        i += 2
    else:
        if sticks[i] == '(':
            stack.append(sticks[i])
            cnt += 1
        else:
            stack.pop()
        i += 1

print(cnt)