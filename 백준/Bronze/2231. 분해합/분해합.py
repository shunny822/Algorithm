n = int(input())
start_n = 0 if n < 18 else n - 9*len(str(n))
for num in range(start_n, n):
    sum_n = 0
    for m in str(num):
        sum_n += int(m)
    if num + sum_n == n:
        print(num)
        break
else:
    print(0)