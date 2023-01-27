import sys

r = set()
for _ in range(10):
    r.add(int(sys.stdin.readline())%42)
print(len(r))