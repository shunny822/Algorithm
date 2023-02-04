import sys

input()
n = set(map(int, sys.stdin.readline().split()))
input()
m = list(map(int, sys.stdin.readline().split()))

same_n = n & set(m)
for num in m:
    print(1 if num in same_n else 0)