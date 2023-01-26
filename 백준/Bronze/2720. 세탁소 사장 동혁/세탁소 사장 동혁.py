import sys

t = int(input())
for i in range(t):
    c = int(sys.stdin.readline())
    change = []
    change.append(c//25)
    c -= change[0]*25
    change.append(c//10)
    c -= change[1]*10
    change.append(c//5)
    c -= change[2]*5
    change.append(c)
    print(*change)