import sys

input()
a = set(sys.stdin.readline().split())
b = set(sys.stdin.readline().split())
print(len(a^b))