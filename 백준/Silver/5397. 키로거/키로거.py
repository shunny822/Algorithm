import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    string = input().rstrip()
    left = deque()
    right = deque()

    for s in string:
        if s == '<':
            if left:
                right.appendleft(left.pop())
        elif s == '>':
            if right:
                left.append(right.popleft())
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)
    
    print(''.join(left), ''.join(right), sep='')