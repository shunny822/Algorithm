import sys

t = int(input())
for i in range(t):
    n = int(sys.stdin.readline())
    print(sum(list(map(int, sys.stdin.readline().split()))))