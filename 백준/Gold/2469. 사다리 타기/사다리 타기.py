import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
origin_arr = [chr(i) for i in range(65, 65+k)]
res_arr = list(input().rstrip())
ladder = [input().rstrip() for _ in range(n)]

for i in range(n):
    line = ladder[i]
    if line == '?'*(k-1):
        break
    for j in range(k-1):
        if line[j] == '-':
            origin_arr[j], origin_arr[j+1] = origin_arr[j+1], origin_arr[j]

for i in reversed(range(n)):
    line = ladder[i]
    if line == '?'*(k-1):
        break
    for j in range(k-1):
        if line[j] == '-':
            res_arr[j], res_arr[j+1] = res_arr[j+1], res_arr[j]

ans = ''
index = 0
while index < k-1:
    if origin_arr[index] == res_arr[index]:
        ans += '*'
        index += 1
    else:
        if origin_arr[index] == res_arr[index+1] and origin_arr[index+1] == res_arr[index]:
            ans += '-*'
            index += 2
        else:
            print('x'*(k-1))
            break
else:
    print(ans[:k-1])