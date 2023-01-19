import sys

remain = {}
t = int(input())

for i in range(t):
    name, io = sys.stdin.readline().split()
    if io == 'leave':
        remain.pop(name)
    else:
        remain[name] = io

names = sorted(remain.keys())
print(*names[::-1], sep='\n')