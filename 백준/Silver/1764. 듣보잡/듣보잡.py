import sys
input = sys.stdin.readline

m, n = map(int, input().split())
a = set(input().rstrip() for _ in range(m))
b = set(input().rstrip() for _ in range(n))
ab = a & b
print(len(ab), *sorted(list(ab)), sep='\n')