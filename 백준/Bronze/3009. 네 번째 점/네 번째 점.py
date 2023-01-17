import sys

xy = list(map(int, sys.stdin.read().split()))
x = xy[::2]
y = xy[1::2]

for i in x:
    if x.count(i) == 1:
        print(i, end=' ')
        break
for i in y:
    if y.count(i) == 1:
        print(i, end=' ')
        break