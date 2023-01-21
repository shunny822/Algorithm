a, b = input().split()
A = int(a[2] + a[1] + a[0])
B = int(b[2] + b[1] + b[0])
print(A if A > B else B)