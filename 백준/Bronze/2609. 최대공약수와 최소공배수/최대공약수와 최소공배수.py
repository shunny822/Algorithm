def common_d(a, b):
    if a % b == 0:
        return b
    else:
        return common_d(b, a % b)

a, b = map(int, input().split())
print(common_d(a, b))
x, y = a, b
while a != b:
    if a < b:
        a += x
    else:
        b += y
print(a)