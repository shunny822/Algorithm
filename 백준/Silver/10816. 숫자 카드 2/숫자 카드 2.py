import sys
input = sys.stdin.readline

input()
sg = {}
for n in map(int, input().split()):
    sg[n] = sg.get(n, 0) + 1

input()
nums = list(map(int, input().split()))

for n in nums:
    print(sg.get(n, 0), end=' ')