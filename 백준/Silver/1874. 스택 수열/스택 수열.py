import sys

n = int(input())
sequence = [int(sys.stdin.readline()) for _ in range(n)]
index = 0
stack = []
num = 1
io = []

for i in range(n*2):
    if stack and stack[-1] == sequence[index]:
        stack.pop()
        io.append('-')
        index += 1
    else:
        stack.append(num)
        io.append('+')
        num += 1

print('NO') if stack else print(*io, sep='\n')