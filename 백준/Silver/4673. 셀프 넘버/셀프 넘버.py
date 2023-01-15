def d(n):
    add_n = n
    while n > 0:
        add_n += n%10
        n //= 10
    return add_n

self_n = set()
for i in range(1, 10001):
    if d(i) <=10000:
        self_n.add(d(i))
not_self = set(range(1, 10001)) - self_n
result = sorted(list(not_self))
print(*result, sep='\n')