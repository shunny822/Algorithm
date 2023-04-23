import sys
input = sys.stdin.readline

n = int(input())
b = [int(input()) for _ in range(n)]
view = []
ans = 0

for i in range(n):
    while view and view[-1] <= b[i]:
        view.pop()
    view.append(b[i])
    ans += len(view) - 1

print(ans)