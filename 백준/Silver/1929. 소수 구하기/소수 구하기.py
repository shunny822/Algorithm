m, n = map(int, input().split())
prime = {i for i in range(m, n+1) if i & 1}
if m < 3:
    prime -= {1}
    prime.add(2)

not_prime = set()
for i in range(3, n//2+1):
    num = i + i
    while num < n+1:
        if num > m-1:
            not_prime.add(num)
        num += i

prime -= not_prime
print(*sorted(list(prime)), sep='\n')