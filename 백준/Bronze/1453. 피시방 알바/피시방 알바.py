import sys

n = int(input())
seat = set(sys.stdin.readline().split())
print(n - len(seat))