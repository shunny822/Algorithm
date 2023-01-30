import sys

a, b = sys.stdin.readline().split()
a = [int(x) for x in a]
b = [int(x) for x in b]
sum_n = sum(b)
total = 0
for n in a:
    total += n*sum_n
print(total)