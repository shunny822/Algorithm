import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
score = []

for i in range(len(s)):
    if s[i] == '(':
        if len(stack) == len(score):
            score.append([2])
        else:
            score[len(stack)].append(2)
        stack.append(s[i])
    elif s[i] == '[':
        if len(stack) == len(score):
            score.append([3])
        else:
            score[len(stack)].append(3)
        stack.append(s[i])
    elif stack and ((s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[')):
        if len(stack) == len(score):
            stack.pop()
        else:
            x = sum(score.pop())
            score[-1][-1] *= x
            stack.pop()
    else:
        stack.append(s[i])
        break

print(0 if stack else sum(score[0]))