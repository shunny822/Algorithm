import sys

n = int(input())
sequence = [int(sys.stdin.readline()) for _ in range(n)]
index = 0
stack = []
num = 1
io = []

while len(io) < n*2:
    if num == sequence[index]:
        io.append('+')
        io.append('-')
        num += 1
        index += 1
    elif stack and stack[-1] == sequence[index]:
        stack.pop()
        io.append('-')
        index += 1
    else:
        stack.append(num)
        io.append('+')
        num += 1

print('NO') if stack else print(*io, sep='\n')