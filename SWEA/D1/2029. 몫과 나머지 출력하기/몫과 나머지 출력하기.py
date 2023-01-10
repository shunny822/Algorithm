t = int(input())

for i in range(1, t+1):
    a, b = input().split()
    x, y = divmod(int(a), int(b))
    print(f'#{i} {x} {y}')