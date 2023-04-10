import sys
input = sys.stdin.readline

n = input().rstrip().replace(' ', '')
n += n
target = int(min(n[0:4], n[1:5], n[2:6], n[3:7]))
check = [False] * 10000
cnt = 0

for i in range(1111, 10000):
    if i == target:
        print(cnt + 1)
        break

    if '0' in str(i):
        continue

    if not check[i]:
        cnt += 1
        temp = str(i) * 2
        for j in range(4):
            check[int(temp[j:j+4])] = True