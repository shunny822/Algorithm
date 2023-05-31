import sys
input = sys.stdin.readline

s = input().rstrip()
parts = {s}
for l in range(1, len(s)):
    for i in range(len(s)-l+1):
        parts.add(s[i:i+l])

print(len(parts))