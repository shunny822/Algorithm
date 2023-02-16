import sys
input = sys.stdin.readline

s = input().rstrip()
l1 = len(s)
search = input().rstrip()
l2 = len(search)
cnt = 0
x = 0

while x <= l1 - l2:
    if s[x:x+l2] == search:
        cnt += 1
        x += l2
    else:
        x += 1
print(cnt)