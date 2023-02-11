import sys

l = int(input())
s = sys.stdin.readline().rstrip()
h = 0
for i in range(l):
    h += (ord(s[i])-96)*(31**i)

print(h%1234567891)