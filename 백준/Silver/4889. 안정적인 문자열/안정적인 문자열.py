import sys
input = sys.stdin.readline

turn = 0
while 1:
    turn += 1
    S = input().rstrip()
    if S[0] == '-':
        break
    
    stack = []
    cnt = 0
    for s in S:
        if s == '{':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                cnt += 1
                stack.append('{')
    
    ans = cnt + len(stack)//2
    print(f'{turn}. {ans}')