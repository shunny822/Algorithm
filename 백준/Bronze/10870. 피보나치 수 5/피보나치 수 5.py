def fibo(n):
    if n < 2:
        return d[n]
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input())
if n == 0:
    print(0)
else:
    d = [0]*(n+1)
    d[1] = 1
    print(fibo(n))