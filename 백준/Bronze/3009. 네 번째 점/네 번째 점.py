import sys

xy = list(map(int, sys.stdin.read().split()))
if xy[0] == xy[2]:
    print(xy[4], end=' ')
elif xy[0] == xy[4]:
    print(xy[2], end=' ')
else:
    print(xy[0], end=' ')
if xy[1] == xy[3]:
    print(xy[5])
elif xy[1] == xy[5]:
    print(xy[3])
else:
    print(xy[1])