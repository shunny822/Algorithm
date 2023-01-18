import sys

t = int(input())
for i in range(t):
    s_list = sys.stdin.readline().split()
    for s in s_list:
        print(s[-1::-1], end=' ')
    print()