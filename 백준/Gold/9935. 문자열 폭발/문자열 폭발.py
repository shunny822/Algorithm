import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()
l = len(bomb)
stack = []

for s in string:
    stack.append(s)

    if stack[-1] == bomb[-1]:
        temp = ''

        for _ in range(l):
            temp = stack.pop() + temp

            if len(stack) == 0:
                break
        
        if temp != bomb:
            for t in temp:
                stack.append(t)

print(''.join(stack)) if stack else print('FRULA')