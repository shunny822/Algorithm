import sys

chars = list(sys.stdin.readline().strip())
for i, s in enumerate(chars):
    print(s, end='')
    if i % 10 == 9:
        print()