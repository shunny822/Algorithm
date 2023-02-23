import sys

m = int(input())
s = set()
for _ in range(m):
    order = sys.stdin.readline().rstrip()

    if 'add' in order:
        order, x = order.split()
        s.add(int(x))
    elif 'remove' in order:
        order, x = order.split()
        s.discard(int(x))
    elif 'check' in order:
        order, x = order.split()
        print(1 if int(x) in s else 0)
    elif 'toggle' in order:
        order, x = order.split()
        if int(x) in s:
            s.remove(int(x))
        else:
            s.add(int(x))
    elif order == 'all':
        s = {i for i in range(1, 21)}
    elif order == 'empty':
        s = set()