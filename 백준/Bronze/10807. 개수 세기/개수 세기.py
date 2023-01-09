amount = int(input())
numbers = input().split()
a = input()
cnt = 0

for i in range(amount):
    if a == numbers[i]:
        cnt += 1

print(cnt)