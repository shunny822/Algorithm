import sys

n = int(input())
members = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])
for i in range(n):
    print(*members[i])