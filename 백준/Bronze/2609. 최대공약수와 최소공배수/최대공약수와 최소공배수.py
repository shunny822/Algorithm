a, b = map(int, input().split())
A = set()
B = set()

for i in range(1, int(a**(1/2))+1):
    if a % i == 0:
        A.add(a//i)
        A.add(i)
for i in range(1, int(b**(1/2))+1):
    if b % i == 0:
        B.add(b//i)
        B.add(i)
print(max(A&B))

x = a
y = b
while x != y:
    if x < y:
        x += a
    else:
        y += b
print(x)