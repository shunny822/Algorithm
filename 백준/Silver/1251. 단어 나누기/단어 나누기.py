import sys

s = list(sys.stdin.readline().rstrip())
new_s = []

for i in range(0, len(s)-2):
    for j in range(i+1, len(s)-1):
        one = reversed(s[:i+1])
        two = reversed(s[i+1:j+1])
        three = reversed(s[j+1:])
        new_s.append(''.join(one)+''.join(two)+''.join(three))

print(sorted(new_s)[0])