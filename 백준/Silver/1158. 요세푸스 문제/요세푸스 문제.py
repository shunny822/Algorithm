import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = [str(i) for i in range(1, n+1)]
res = []
index = 0
cnt = 1

while numbers:
    if index == n:
        index -= n
    
    if cnt == k:
        res.append(numbers.pop(index))
        n -= 1
        cnt = 0
    else:
        index += 1
    
    cnt += 1

print('<' + ', '.join(res) + '>')