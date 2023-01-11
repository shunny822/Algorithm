num = int(input())
result = 0
while num > 0:
    result += num%10
    num //= 10
print(result)