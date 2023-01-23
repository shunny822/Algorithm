m, n = map(int, input().split())
not_prime = {1}
for i in range(2, n//2+1):
    k = i + i
    while k < n+1:
        if k >= m:
            not_prime.add(k)
        k += i

for j in range(m, n+1):
    if j not in not_prime:
        print(j)