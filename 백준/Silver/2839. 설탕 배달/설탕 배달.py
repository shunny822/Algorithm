n = int(input())
cnt3 = 0
while n > 0:
    if n % 5 == 0:
        break
    n -= 3
    cnt3 += 1

print(cnt3 + n//5 if n%5 == 0 else -1)