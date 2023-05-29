import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    num = [input().rstrip() for _ in range(n)]
    num.sort()
    for j in range(n-1):
        if len(num[j]) <= len(num[j+1]) and num[j] == num[j+1][:len(num[j])]:
            print('NO')
            break
    else:
        print('YES')