import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(n):
    char = []
    s = input().strip()
    char.append(s[0])
    for j in range(1, len(s)):
        if s[j] == s[j-1]:
            continue
        else:
            if s[j] not in char:
                char.append(s[j])
            else:
                break
    else:
        cnt += 1
print(cnt)