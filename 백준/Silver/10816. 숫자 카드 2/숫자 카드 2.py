import sys

n = int(input())
sang = {}
for num in sys.stdin.readline().split():
    if int(num) in sang:
        sang[int(num)] += 1
    else:
        sang[int(num)] = 1

m = int(input())
card = list(map(int, sys.stdin.readline().split()))
for c in card:
    print(sang.get(c, 0), end=' ')