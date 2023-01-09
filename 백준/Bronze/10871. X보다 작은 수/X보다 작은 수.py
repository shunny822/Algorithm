n, x = map(int, input().split())
numbers = list(map(int, input().split()))
small_num = []

for i in range(n):
    if numbers[i] < x:
        small_num.append(numbers[i])

for num in small_num:
    print(num, end=' ')