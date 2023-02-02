import sys

m = int(input())
cups = {'1': 0, '2': 1, '3': 2}
for _ in range(m):
    a, b = sys.stdin.readline().split()
    cups[a], cups[b] = cups[b], cups[a]

for k in cups:
    if cups[k] == 0:
        print(k)