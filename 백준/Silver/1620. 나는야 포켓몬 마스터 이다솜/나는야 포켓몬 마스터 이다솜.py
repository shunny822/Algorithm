import sys
input = sys.stdin.readline

n, m = map(int,input().split())
monster = {}

for i in range(1, n+1):
    name = input().rstrip()
    monster[str(i)] = name
    monster[name] = str(i)

for _ in range(m):
    print(monster[input().rstrip()])