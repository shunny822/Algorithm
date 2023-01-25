import sys

n = int(input())
num = []

for _ in range(n):
    order = sys.stdin.readline().rstrip()
    if 'push' in order:
        push, number = order.split()
        num.append(number)
    elif order == 'pop':
        try:
            print(num.pop())
        except:
            print(-1)
    elif order == 'size':
        print(len(num))
    elif order == 'empty':
        print(0 if num else 1)
    elif order == 'top':
        try:
            print(num[-1])
        except:
            print(-1)