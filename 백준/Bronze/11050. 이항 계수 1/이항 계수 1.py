def fac(n=int):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n, k = map(int, input().split())
print(fac(n)//(fac(k)*fac(n-k)))