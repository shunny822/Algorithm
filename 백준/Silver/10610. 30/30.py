N = list(input())
zero = False
total = 0

for s in N:
    n = int(s)
    total += n
    if n == 0: zero = True

if zero and total%3 == 0:
    print(''.join(sorted(N, reverse=True)))
else:
    print(-1)